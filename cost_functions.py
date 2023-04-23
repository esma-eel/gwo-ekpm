import datetime
from utils import knbrs, safe_ln
import networkx as nx
from constants import IMPACT_RANGE
from utils import graph_nodes


def fitness_function(seed_set, graph, propogation_probability):  # wolf,
    start = datetime.datetime.now()
    """
    calculating the fitness value for 'wolf'
    based on part 4.1 equation 13 in article
    """
    impact_range = IMPACT_RANGE
    # Creating s' set with using each item in seed set
    s_prim = []
    seed_set_with_neighbors = {}
    for seed_set_item in seed_set:
        seed_set_item_neighbors = knbrs(graph, seed_set_item, 2)
        seed_set_with_neighbors[seed_set_item] = seed_set_item_neighbors
        s_prim += list(seed_set_item_neighbors)

    s_prim = set(s_prim)

    for node in set(s_prim):
        neighbors = knbrs(graph, node, 1)
        for neighbor in neighbors:
            edge_data = graph.get_edge_data(neighbor, node).get("days")
            if edge_data < impact_range and neighbor in s_prim:
                s_prim.remove(neighbor)

    s_prim_graph = graph.subgraph(s_prim)
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

    prb = propogation_probability
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
        # seed_set_item_neighbors = knbrs(graph, seed_set_item, 2)
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
    print({"action": "calculate_fitness", "time": str(delta)})
    return -(fitness)


def fitness_function_reverse(seed_set, graph, propogation_probability):  # wolf,
    start = datetime.datetime.now()
    """
    calculating the fitness value for 'wolf'
    based on part 4.1 equation 13 in article
    """
    impact_range = IMPACT_RANGE
    # Creating s' set with using each item in seed set
    s_prim = []
    seed_set_with_neighbors = {}
    for seed_set_item in seed_set:
        seed_set_item_neighbors = knbrs(graph, seed_set_item, 2)
        seed_set_with_neighbors[seed_set_item] = seed_set_item_neighbors
        s_prim += list(seed_set_item_neighbors)

    s_prim = set(s_prim)

    for node in set(s_prim):
        neighbors = knbrs(graph, node, 1)
        for neighbor in neighbors:
            edge_data = graph.get_edge_data(neighbor, node).get("days")
            if edge_data > impact_range and neighbor in s_prim:
                s_prim.remove(neighbor)

    s_prim_graph = graph.subgraph(s_prim)
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

    prb = propogation_probability
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
        # seed_set_item_neighbors = knbrs(graph, seed_set_item, 2)
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
    print({"action": "calculate_fitness", "time": str(delta)})
    return -(fitness)


def calculate_i_for_vj(node, seed_set, position, graph):
    nodes_list = graph_nodes(graph)
    first_order_neighbors = knbrs(graph, node, 1)
    second_order_neighbors_unclean = knbrs(graph, node, 2)
    second_order_neighbors = set()
    for ng in second_order_neighbors_unclean:
        if ng not in first_order_neighbors:
            second_order_neighbors.add(ng)

    sum_first_order_neighbors = 0
    sum_second_order_neighbors = 0

    for i in seed_set:
        sum_first_order_neighbors += position[nodes_list.index(i)]

    for i in seed_set:
        for k in seed_set:
            if i == k:
                continue

            sum_second_order_neighbors += (
                position[nodes_list.index(i)] * position[nodes_list.index(k)]
            )

    return sum_first_order_neighbors + sum_second_order_neighbors


def calculate_w_for_vj(node, seed_set, position, graph):
    i_for_vj = calculate_i_for_vj(node, seed_set, position, graph)
    degree_of_vj = graph.degree(node)

    return i_for_vj * degree_of_vj


def calculate_W_for_S(s_prim, seed_set, position, graph):
    sum_w_of_s_prim_nodes = 0
    for vj in s_prim:
        sum_w_of_s_prim_nodes += calculate_w_for_vj(
            vj, seed_set, position, graph
        )

    return sum_w_of_s_prim_nodes


def gwim_fitness_function(wolf, graph):
    start = datetime.datetime.now()
    seed_set = wolf.S
    position = wolf.X

    s_prim = []
    for seed_set_item in seed_set:
        seed_set_item_neighbors = knbrs(graph, seed_set_item, 2)
        s_prim += list(seed_set_item_neighbors)

    s_prim = set(s_prim)

    sum_of_entropy = 0
    WS = calculate_W_for_S(s_prim, seed_set, position, graph)

    for vj in s_prim:
        wvj = calculate_w_for_vj(vj, seed_set, position, graph)
        wvj_divide_WS = wvj / WS
        wvj_divide_WS_ln = safe_ln(wvj_divide_WS)
        wvj_WS = wvj_divide_WS * wvj_divide_WS_ln
        sum_of_entropy += wvj_WS

    end = datetime.datetime.now()
    delta = end - start
    print({"action": "calculate_fitness", "time": str(delta)})

    return -sum_of_entropy
