import math
import random

import networkx as nx
import numpy as np

print("test11")
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
k = 10  # number of seed set
population_size = 50  # population size or n which is used in article
max_t = 50  # maximum number of iterations
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

# propogation probability for independent cascade -> probability to active nodes
propogation_probability = 0.02
monte_carlo_simulation_number = 50


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
            print(new_active)
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


def probability_of_node_gets_message(wolf, seed_set, v_prim_graph):
    """
    calculating the probability of 'wolf' getting activation message
    based on part 4.1 equation 10 in article
    """
    iwolf = 0
    total_p_wolf_to_neighbor = 0
    total_p_wolf_to_second_order_neighbor = 0
    for neighbor in v_prim_graph.neighbors(wolf):
        p_wolf_to_neighbor = 1 / v_prim_graph.number_of_edges(wolf, neighbor)
        if neighbor in seed_set:
            total_p_wolf_to_neighbor += p_wolf_to_neighbor

        for second_order_neigbor in v_prim_graph.neighbors(neighbor):
            if second_order_neigbor in seed_set:
                p_second_neighbor_to_neighbor = (
                    1
                    / v_prim_graph.number_of_edges(
                        second_order_neigbor, neighbor
                    )
                )

                total_p_wolf_to_second_order_neighbor += (
                    p_second_neighbor_to_neighbor * p_wolf_to_neighbor
                )

    iwolf = total_p_wolf_to_neighbor + total_p_wolf_to_second_order_neighbor
    return iwolf


def worthiness_of_wolf(wolf, seed_set, v_prim_graph):
    """
    calculating the worthiness for 'wolf'
    based on part 4.1 equation 11 in article
    """
    iwolf = probability_of_node_gets_message(wolf, seed_set, v_prim_graph)
    worthiness = iwolf * v_prim_graph.degree(wolf)
    return worthiness


def sum_worthiness(wolf, seed_set, v_prim_graph):
    """
    calculating the total worth of 'wolf'
    based on part 4.1 equation 12 in article
    """
    worth = 0
    for neighbor_wolf in v_prim_graph.neighbors(wolf):
        worth += worthiness_of_wolf(neighbor_wolf, seed_set, v_prim_graph)

    return worth


def fitness_function(wolf, seed_set, v_prim_graph):
    """
    calculating the fitness value for 'wolf'
    based on part 4.1 equation 13 in article
    """
    # generate subgraph based on the timing in dataset file
    # first subgraph
    fitness = 0
    general_worth = sum_worthiness(wolf, seed_set, v_prim_graph)
    for neighbor_wolf in v_prim_graph.neighbors(wolf):
        neighbor_wolf_worth = worthiness_of_wolf(
            neighbor_wolf, seed_set, v_prim_graph
        )
        try:
            neighbor_worth_divide_by_general = (
                neighbor_wolf_worth / general_worth
            )
        except ZeroDivisionError:
            neighbor_worth_divide_by_general = 0
        fitness += neighbor_worth_divide_by_general * safe_ln(
            neighbor_worth_divide_by_general
        )

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
    wolf_position = v_prim_graph.nodes[wolf]["position"]
    new_position = wolf_position

    alpha_position = v_prim_graph.nodes[alpha]["position"]
    alpha_A1 = v_prim_graph.nodes[alpha]["A"]
    alpha_C1 = v_prim_graph.nodes[alpha]["C"]

    beta_position = v_prim_graph.nodes[beta]["position"]
    beta_A1 = v_prim_graph.nodes[beta]["A"]
    beta_C1 = v_prim_graph.nodes[beta]["C"]

    delta_position = v_prim_graph.nodes[delta]["position"]
    delta_A1 = v_prim_graph.nodes[delta]["A"]
    delta_C1 = v_prim_graph.nodes[delta]["C"]

    for j in range(0, len(v_prim_graph)):
        daj = abs((alpha_C1 * alpha_position[j]) - wolf_position[j])
        y1 = alpha_position[j] - (alpha_A1 * daj)

        dbj = abs((beta_C1 * beta_position[j]) - wolf_position[j])
        y2 = beta_position[j] - (beta_A1 * dbj)

        ddj = abs((delta_C1 * delta_position[j]) - wolf_position[j])
        y3 = delta_position[j] - (delta_A1 * ddj)

        new_position[j] = abs((y1 + y2 + y3) / 3)

    return new_position


def generate_control_parameters(t, v_prim_graph):
    a = 2 - 2 * (t / max_t)
    for node in v_prim_graph.nodes():
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)
        A = (2 * a) * r1 - a
        C = 2 * r2
        nx.set_node_attributes(v_prim_graph, {node: r1}, name="r1")
        nx.set_node_attributes(v_prim_graph, {node: r2}, name="r2")
        nx.set_node_attributes(v_prim_graph, {node: A}, name="A")
        nx.set_node_attributes(v_prim_graph, {node: C}, name="C")

    print("generating control parameters for nodes completed in iteration: ", t)


every_alpha = []


def main():
    """
    main function of gwim algorithm and running independent cascade for
    alpha wolf seed set
    """
    # iteration counter
    t = 0
    # generating control parameters
    print("generating control parameters iteration: ", t)
    generate_control_parameters(t, v_prim_graph)

    print("creating population before starting main algorithm:")
    # -- how to select population --> degrees more than 2 or
    # random step for list
    # check a parameter again
    graph_nodes = list(v_prim_graph.nodes())
    population = random.sample(graph_nodes, population_size)
    for wolf in population:
        print("generating random position for wolf: ", wolf)
        position_value, seed_set_value = wolf_random_position(v_prim_graph, k)
        nx.set_node_attributes(
            v_prim_graph, {wolf: position_value}, name="position"
        )
        print("generating random seed set for wolf: ", wolf)
        nx.set_node_attributes(
            v_prim_graph, {wolf: seed_set_value}, name="seed_set"
        )
        print("generating fitness value for wolf: ", wolf)
        fitness_value = fitness_function(wolf, seed_set_value, v_prim_graph)
        nx.set_node_attributes(
            v_prim_graph, {wolf: fitness_value}, name="value"
        )

    print("extracting alpha, beta, delta and omega wolves:")
    population_sorted = sorted(
        population,
        key=lambda wolf: v_prim_graph.nodes[wolf]["value"],
        reverse=True,
    )
    alpha, beta, delta = population_sorted[:3]
    omega_wolves = population_sorted[3:]

    v_prim_graph_list = list(v_prim_graph)

    while t < max_t:
        print(f"---------- iteration {t} -----------")
        for omega_wolf in omega_wolves:
            print("updating position for wolf: ", omega_wolf)
            position_value = wolf_update_position(
                v_prim_graph, omega_wolf, alpha, beta, delta
            )
            nx.set_node_attributes(
                v_prim_graph, {omega_wolf: position_value}, name="position"
            )
            print("updating seed set for wolf: ", omega_wolf)
            seed_set_value = get_corresponding_seed_set(
                v_prim_graph_list, position_value, k
            )
            nx.set_node_attributes(
                v_prim_graph, {omega_wolf: seed_set_value}, name="seed_set"
            )

        print("generating control parameters iteration: ", t)
        generate_control_parameters(t, v_prim_graph)

        for wolf in population:
            print("recalculating fitness value for wolf: ", wolf)
            seed_set_value = v_prim_graph.nodes[wolf]["seed_set"]
            fitness_value = fitness_function(wolf, seed_set_value, v_prim_graph)
            nx.set_node_attributes(
                v_prim_graph, {wolf: fitness_value}, name="value"
            )

        print("extracting alpha, beta, delta and omega wolves:")
        population_sorted = sorted(
            population,
            key=lambda wolf: v_prim_graph.nodes[wolf]["value"],
            reverse=True,
        )
        alpha, beta, delta = population_sorted[:3]
        if alpha not in every_alpha:
            every_alpha.append(alpha)
        omega_wolves = population_sorted[3:]
        if (
            v_prim_graph.nodes[beta]["position"]
            == v_prim_graph.nodes[alpha]["position"]
        ) or (
            v_prim_graph.nodes[delta]["position"]
            == v_prim_graph.nodes[beta]["position"]
        ):
            print("regenerating position for wolf beta: ", beta)
            position_value, seed_set_value = wolf_random_position(
                v_prim_graph, k
            )
            nx.set_node_attributes(
                v_prim_graph, {beta: position_value}, name="position"
            )
            print("regenerating position for wolf delta: ", delta)
            position_value, seed_set_value = wolf_random_position(
                v_prim_graph, k
            )
            nx.set_node_attributes(
                v_prim_graph, {delta: position_value}, name="position"
            )

        t += 1

    for index, wolf in enumerate(population):
        print(
            f"index[{index}]",
            wolf,
            # v_prim_graph.nodes[wolf]["position"],
            v_prim_graph.nodes[wolf]["value"],
            v_prim_graph.nodes[wolf]["seed_set"],
        )

    print("Final Alpha is:")
    print(
        alpha,
        # v_prim_graph.nodes[alpha]["position"],
        v_prim_graph.nodes[alpha]["value"],
        v_prim_graph.nodes[alpha]["seed_set"],
    )
    print("all unique alpha throgh iterations are: ")
    for u_alpha in every_alpha:
        print(
            u_alpha,
            # v_prim_graph.nodes[alpha]["position"],
            v_prim_graph.nodes[u_alpha]["value"],
            v_prim_graph.nodes[u_alpha]["seed_set"],
        )
    print("running simulation of independent cascade:")
    independent_cascade_result = independent_cascade_simulation(
        v_prim_graph=v_prim_graph,
        seed_set=v_prim_graph.nodes[alpha]["seed_set"],
        propogation_probability=propogation_probability,
        monte_carlo_simulation_number=monte_carlo_simulation_number,
    )

    print("independent cascade simulation result is:")
    print(independent_cascade_result)

    return alpha


if __name__ == "__main__":
    main()
