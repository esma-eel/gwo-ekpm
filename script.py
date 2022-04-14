import copy
import math
import random

import networkx as net

# dataset filename
file_name = "dataset/CA-AstroPh.txt"

# crating undirected graph based on dataset
graph_type = net.Graph()

G = net.read_edgelist(
    file_name,
    create_using=graph_type,
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

print(len(v_prim_list))
print(len(v_1_degree))

v_prim_graph = G.subgraph(v_prim_list)

# propogation probability for independent cascade -> probability to active nodes
propogation_probability = 0.02


def independent_cascade_simulation(
    v_prim_graph, seed_set, propogation_probability
):
    """
    independent cascade function in order to simulate propogation
    with seed set of alpha wolf found from Gwim
    """
    new_active = True
    current_active_nodes = copy.deepcopy(seed_set)
    new_active_nodes = set()
    activated_nodes = copy.deepcopy(seed_set)
    influence_spread = len(seed_set)

    print("current active nodes are:", current_active_nodes)
    print("activated nodes are: ", activated_nodes)
    print("influence spread number is: ", influence_spread)

    while new_active:
        for node in current_active_nodes:
            print("current active node in loop is: ", node)
            for neighbor in v_prim_graph.neighbors(node):
                print(f"current neighbor for node {node} is: ", neighbor)
                if neighbor not in activated_nodes:
                    print(f"neighbor {neighbor} not in activated nodes")
                    if flip_the_coin(propogation_probability):
                        print(f"neighbor {neighbor} of node {node} activated")
                        new_active_nodes.add(neighbor)
                        activated_nodes.append(neighbor)
        old_influence_spread = influence_spread
        influence_spread += len(new_active_nodes)
        print(
            f"influence spread from {old_influence_spread} updated to"
            f" {influence_spread}"
        )
        if new_active_nodes:
            print("updating current active nodes")
            current_active_nodes = list(new_active_nodes)
            print("resetting new_active_nodes for next iteration")
            new_active_nodes = set()
        else:
            print("there is no active node left")
            new_active = False

    return influence_spread


def flip_the_coin(probability):
    """
    if result of this function is True the node will be activated
    in independent cascade
    """
    return random.random() < probability


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
    fitness = 0
    general_worth = sum_worthiness(wolf, seed_set, v_prim_graph)

    for neighbor_wolf in v_prim_graph.neighbors(wolf):
        neighbor_wolf_worth = worthiness_of_wolf(
            neighbor_wolf, seed_set, v_prim_graph
        )
        neighbor_worth_divide_by_general = neighbor_wolf_worth / general_worth
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
        net.set_node_attributes(v_prim_graph, {node: r1}, name="r1")
        net.set_node_attributes(v_prim_graph, {node: r2}, name="r2")
        net.set_node_attributes(v_prim_graph, {node: A}, name="A")
        net.set_node_attributes(v_prim_graph, {node: C}, name="C")

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
    population = list(v_prim_graph.nodes())[:population_size]
    for wolf in population:
        print("generating random position for wolf: ", wolf)
        position_value, seed_set_value = wolf_random_position(v_prim_graph, k)
        net.set_node_attributes(
            v_prim_graph, {wolf: position_value}, name="position"
        )
        print("generating random seed set for wolf: ", wolf)
        net.set_node_attributes(
            v_prim_graph, {wolf: seed_set_value}, name="seed_set"
        )
        print("generating fitness value for wolf: ", wolf)
        fitness_value = fitness_function(wolf, seed_set_value, v_prim_graph)
        net.set_node_attributes(
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
            net.set_node_attributes(
                v_prim_graph, {omega_wolf: position_value}, name="position"
            )
            print("updating seed set for wolf: ", omega_wolf)
            seed_set_value = get_corresponding_seed_set(
                v_prim_graph_list, position_value, k
            )
            net.set_node_attributes(
                v_prim_graph, {omega_wolf: seed_set_value}, name="seed_set"
            )

        print("generating control parameters iteration: ", t)
        generate_control_parameters(t, v_prim_graph)

        for wolf in population:
            print("recalculating fitness value for wolf: ", wolf)
            seed_set_value = v_prim_graph.nodes[wolf]["seed_set"]
            fitness_value = fitness_function(wolf, seed_set_value, v_prim_graph)
            net.set_node_attributes(
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
            net.set_node_attributes(
                v_prim_graph, {beta: position_value}, name="position"
            )
            print("regenerating position for wolf delta: ", delta)
            position_value, seed_set_value = wolf_random_position(
                v_prim_graph, k
            )
            net.set_node_attributes(
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
        v_prim_graph,
        v_prim_graph.nodes[alpha]["seed_set"],
        propogation_probability,
    )

    print("independent cascade simulation result is:")
    print(independent_cascade_result)

    return alpha


if __name__ == "__main__":
    main()
