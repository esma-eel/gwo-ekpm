import math
import random
import datetime

import networkx as nx
import numpy as np

# import sys

print("script16")
# dataset filename
file_name = "dataset/CA-AstroPh3.tsv"
# file_with_timing = pd.read_csv(file_name, sep='\t')

# crating undirected graph based on dataset
graph_type = nx.Graph()

G = nx.read_edgelist(
    file_name,
    create_using=graph_type,
    data=(("days", int),),
    nodetype=int,
)
k = 40  # number of seed set
population_size = 50  # population size or n which is used in article
max_t = 100  # maximum number of iterations

print("K = ", k)
print("Population = ", population_size)
print("MAX_T = ", max_t)


v_prim_list = []  # using this list in order to seperate nodes with degree >= 2
v_1_degree = []  # this list is informational, keeps node with degree 1

#  creating new graph named v_prim by using nodes with degree higher than 1
for node in G:
    if G.degree(node) > 1:
        v_prim_list.append(node)
    else:
        v_1_degree.append(node)

print("nodes with degree higher than 1:", len(v_prim_list))
print("nodes with degree of 1", len(v_1_degree))

v_prim_graph = G.subgraph(v_prim_list)
v_prim_graph = nx.Graph(v_prim_graph)
v_prim_graph.remove_edges_from(list(nx.selfloop_edges(v_prim_graph)))
print(len(v_prim_graph.nodes))


# propogation probability for independent cascade -> probability to active nodes
propogation_probability = 0.02
print("propogation probability: ", propogation_probability)
monte_carlo_simulation_number = 50
print("simulation iteration number: ", monte_carlo_simulation_number)


def independent_cascade_simulation(
    v_prim_graph,
    seed_set,
    propogation_probability=0.5,
    monte_carlo_simulation_number=50,
):
    """
    Input:  graph object, set of seed nodes, propagation probability
            and the number of Monte-Carlo simulations
    Output: average number of nodes influenced by the seed nodes
    """

    # Loop over the Monte-Carlo Simulations
    spread = []
    for i in range(monte_carlo_simulation_number):
        print(
            f"running simulation number {i} "
            f"from {monte_carlo_simulation_number}"
        )
        # Simulate propagation process
        new_active, all_activated_nodes = seed_set[:], seed_set[:]
        while new_active:
            print(f"new active nodes in simulation {i} are: ")
            print(len(new_active))
            # For each newly active node, find its neighbors
            # that become activated
            new_ones = []
            for node in new_active:

                # Determine neighbors that become infected
                np.random.seed(i)
                # for directed graph use ==> neighbors(node, mode="out")
                # and for undirected graph remove it
                # make sure you make neighbors output as list with list(output)
                success = (
                    np.random.uniform(
                        0, 1, len(list(v_prim_graph.neighbors(node)))
                    )
                    < propogation_probability
                )

                array_of_neighbors = np.array(
                    list(v_prim_graph.neighbors(node))
                )
                new_ones += list(np.extract(success, array_of_neighbors))

            new_active = list(set(new_ones) - set(all_activated_nodes))

            # Add newly activated nodes to the set of activated nodes
            all_activated_nodes += new_active

        spread.append(len(all_activated_nodes))

    return np.mean(spread)


def safe_ln(value):
    """
    function to calculate natural log of value more safe
    """

    if value <= 0:
        return 0

    return math.log(value)


def knbrs(G, start, k):
    nbrs = set([start])
    for _ in range(k):
        nbrs = set((nbr for n in nbrs for nbr in G[n]))

    # In order to prevent any recursion we remove node it self from neighbors
    if start in nbrs:
        nbrs.remove(start)
    return nbrs


def fitness_function(seed_set, v_prim_graph):  # wolf,
    start = datetime.datetime.now()
    """
    calculating the fitness value for 'wolf'
    based on part 4.1 equation 13 in article
    """
    impact_range = 60
    # Creating s' set with using each item in seed set
    s_prim = []
    seed_set_with_neighbors = {}
    for seed_set_item in seed_set:
        seed_set_item_neighbors = knbrs(v_prim_graph, seed_set_item, 2)
        seed_set_with_neighbors[seed_set_item] = seed_set_item_neighbors
        s_prim += list(seed_set_item_neighbors)

    s_prim = set(s_prim)

    for node in set(s_prim):
        neighbors = knbrs(v_prim_graph, node, 1)
        for neighbor in neighbors:
            edge_data = v_prim_graph.get_edge_data(neighbor, node).get("days")
            # نحوه ارتباط برعکس در نظر گرفته شود -- بررسی نتیجه
            if edge_data < impact_range and neighbor in s_prim:
                s_prim.remove(neighbor)

    s_prim_graph = v_prim_graph.subgraph(s_prim)
    s_prim_sum_degrees = sum([degree for node, degree in s_prim_graph.degree()])
    s_prim_mean_degrees = s_prim_sum_degrees // len(s_prim)
    # we use k shell in order to remove the nodes below mean degree of s_prim
    filtered_s_prim_graph = nx.k_core(s_prim_graph, k=s_prim_mean_degrees)

    tolerance_range = 6
    s_prim_eigenvector = None
    while not s_prim_eigenvector:
        if tolerance_range >= 0:
            default_fault_tolerance = f"1.0e-{tolerance_range}"
        else:
            default_fault_tolerance = 1

        try:
            s_prim_eigenvector = nx.eigenvector_centrality(
                filtered_s_prim_graph,
                weight="days",
                tol=float(default_fault_tolerance),
            )
        except nx.PowerIterationFailedConvergence:
            tolerance_range -= 1

    prb = 0.02
    s_prim_eigenvector = dict(
        sorted(
            s_prim_eigenvector.items(),
            key=lambda item: item[1] >= prb,
            reverse=True,
        )
    )
    s_prim_eigenvector_worthy = {}
    for (
        seed_set_item,
        seed_set_item_neighbors,
    ) in seed_set_with_neighbors.items():
        # seed_set_item_neighbors = knbrs(v_prim_graph, seed_set_item, 2)
        for node, egv_value in s_prim_eigenvector.items():
            if node in seed_set_item_neighbors:
                s_prim_eigenvector_worthy[node] = egv_value

    fitness = 0
    general_worth = sum(s_prim_eigenvector_worthy.values())

    for node_j, worth_j in s_prim_eigenvector_worthy.items():
        node_j_worth_divide_by_general_worth = worth_j / general_worth
        fitness += node_j_worth_divide_by_general_worth * safe_ln(
            node_j_worth_divide_by_general_worth
        )

    end = datetime.datetime.now()
    delta = end - start
    print("time for calculating fitness: ", delta)
    return -(fitness)


def find_maximum_degree(target_graph):
    """
    calculating the maximum degree in graph
    to use in random position function
    """
    degree_sequence = sorted(
        (d for n, d in target_graph.degree()), reverse=True
    )
    dmax = max(degree_sequence)
    return dmax


def wolf_random_position(v_prim_graph, k):
    """
    generating random position list Xi for wolf i
    generating corresponding seed set i for wolf i
    based on algorithm 3 in article
    """
    v_prim_graph_list = list(v_prim_graph)
    maximum_degree = find_maximum_degree(v_prim_graph)
    xi = []

    for j in range(0, len(v_prim_graph)):
        r = random.uniform(1, v_prim_graph.degree(v_prim_graph_list[j]))
        xi.append(r / maximum_degree)

    si = get_corresponding_seed_set(v_prim_graph_list, xi, k)

    return xi, si


def get_corresponding_seed_set(v_prim_graph_list, xi, k):
    """
    calculating corresponding seed set based on k which is number of seed set
    and Xi position list for wolf i based on algorithm 3 in article
    """
    local_xi = xi[:]
    si = []
    for number in range(k):
        max_xi_index = local_xi.index(max(local_xi))
        local_xi.pop(max_xi_index)

        max_node = v_prim_graph_list[max_xi_index]

        si.append(max_node)

    return si


def wolf_update_position(v_prim_graph, wolf, alpha, beta, delta):
    """
    update position list of wolf i based on alpha, beta, delta wolves
    based on algorithm 4 in article
    """
    wolf_position = wolf.X
    new_position = wolf_position

    alpha_position = alpha.X
    alpha_A1 = alpha.get_params()["A"]
    alpha_C1 = alpha.get_params()["C"]

    beta_position = beta.X
    beta_A1 = beta.get_params()["A"]
    beta_C1 = beta.get_params()["C"]

    delta_position = delta.X
    delta_A1 = delta.get_params()["A"]
    delta_C1 = delta.get_params()["C"]

    for j in range(0, len(v_prim_graph)):
        daj = abs((alpha_C1 * alpha_position[j]) - wolf_position[j])
        y1 = alpha_position[j] - (alpha_A1 * daj)

        dbj = abs((beta_C1 * beta_position[j]) - wolf_position[j])
        y2 = beta_position[j] - (beta_A1 * dbj)

        ddj = abs((delta_C1 * delta_position[j]) - wolf_position[j])
        y3 = delta_position[j] - (delta_A1 * ddj)

        new_position[j] = abs((y1 + y2 + y3) / 3)

    return new_position


every_alpha = []


class Wolf(object):
    def __init__(self, *args, **kwargs):
        self._position = kwargs.get("position")
        self._seed_set = kwargs.get("seed_set")
        self._value = kwargs.get("value")
        self._history = []
        self._params = {"r1": 0, "r2": 0, "A": 0, "C": 0, "t": 0}

    def generate_params(self, t):
        a = 2 - 2 * (t / max_t)
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)
        A = (2 * a) * r1 - a
        C = 2 * r2
        self._params["r1"] = r1
        self._params["r2"] = r2
        self._params["A"] = A
        self._params["C"] = C
        self._params["t"] = t
        return self._params

    def get_params(self):
        return self._params

    @property
    def X(self):
        return self._position

    @X.setter
    def X(self, value):
        self._position = value

    @property
    def S(self):
        return self._seed_set

    @S.setter
    def S(self, value):
        self._seed_set = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._history.append(value)
        self._value = value


def generate_p_between_nodes(v_prim_graph):
    for node in v_prim_graph.nodes():
        ngs = knbrs(v_prim_graph, node, 1)
        for ng in ngs:
            propagation = random.uniform(0, propogation_probability)
            attr = {(node, ng): {"propagation": propagation}}
            nx.set_edge_attributes(v_prim_graph, attr)


def main():
    """
    main function of gwim algorithm and running independent cascade for
    alpha wolf seed set
    """
    # iteration counter
    t = 0
    print("creating population before starting main algorithm:")
    population = [Wolf() for wolf in range(population_size)]
    for index, wolf in enumerate(population):
        print(
            "generating control parameters iteration: ", t, " for wolf: ", index
        )
        wolf.generate_params(t)
        print("generating random position for wolf: ", index)
        position_value, seed_set_value = wolf_random_position(v_prim_graph, k)
        wolf.X = position_value
        print("generating random seed set for wolf: ", index)
        wolf.S = seed_set_value
        print("wolf ", index, " seed set is: ", wolf.S)
        print("generating fitness value for wolf: ", index)
        fitness_value = fitness_function(wolf.S, v_prim_graph)
        print("fitness value of wolf ", index, fitness_value)
        wolf.value = fitness_value

    print("extracting alpha, beta, delta and omega wolves:")
    population_sorted = sorted(
        population,
        key=lambda wolf: wolf.value,
        reverse=True,
    )
    alpha, beta, delta = population_sorted[:3]
    omega_wolves = population_sorted[3:]

    v_prim_graph_list = list(v_prim_graph)

    while t < max_t:
        print(f"---------- iteration {t} -----------")
        for index, omega_wolf in enumerate(omega_wolves):
            print("updating position for omega wolf: ", index)
            position_value = wolf_update_position(
                v_prim_graph, omega_wolf, alpha, beta, delta
            )
            wolf.X = position_value
            print("updating seed set for wolf: ", index)
            seed_set_value = get_corresponding_seed_set(
                v_prim_graph_list, position_value, k
            )
            wolf.S = seed_set_value
            print("wolf ", index, " seed set is: ", wolf.S)

        print("generating control parameters iteration: ", t)
        # generate_control_parameters(t, v_prim_graph)

        for index, wolf in enumerate(population):
            print("recalculating fitness value for wolf: ", index)
            seed_set_value = wolf.S
            fitness_value = fitness_function(wolf.S, v_prim_graph)
            # nx.set_node_attributes(
            #     v_prim_graph, {wolf: fitness_value}, name="value"
            # )
            print("fitness value of wolf ", index, fitness_value)
            wolf.value = fitness_value

        print("extracting alpha, beta, delta and omega wolves:")
        population_sorted = sorted(
            population,
            key=lambda wolf: wolf.value,
            reverse=True,
        )
        alpha, beta, delta = population_sorted[:3]
        if alpha not in every_alpha:
            every_alpha.append(alpha)
        omega_wolves = population_sorted[3:]
        if (beta.X == alpha.X) or (delta.X == beta.X):
            print("regenerating position for wolf beta: ", beta)
            position_value0, seed_set_value0 = wolf_random_position(
                v_prim_graph, k
            )
            beta.X = position_value0
            print("regenerating position for wolf delta: ", delta)
            position_value1, seed_set_value1 = wolf_random_position(
                v_prim_graph, k
            )
            delta.X = position_value1

        t += 1
        for wolf in population:
            wolf.generate_params(t)

    for index, wolf in enumerate(population):
        print(
            f"wolf[{index}]",
            wolf.value,
            wolf.S,
        )

    print("Final Alpha is:")
    print(
        alpha,
        alpha.value,
        alpha.S,
    )
    print("all unique alpha throgh iterations are: ")
    for index, u_alpha in enumerate(every_alpha):
        print(
            f"alpha[{index}]",
            u_alpha,
            u_alpha.value,
            u_alpha.S,
        )
    print("running simulation of independent cascade:")
    independent_cascade_result = independent_cascade_simulation(
        v_prim_graph=v_prim_graph,
        seed_set=alpha.S,
        propogation_probability=propogation_probability,
        monte_carlo_simulation_number=monte_carlo_simulation_number,
    )

    print("independent cascade simulation result is:")
    print(independent_cascade_result)

    return alpha


if __name__ == "__main__":
    start_main = datetime.datetime.now()
    main()
    end_main = datetime.datetime.now()
    delta_main = end_main - start_main
    print("time of execution this algorithm: ", delta_main)
