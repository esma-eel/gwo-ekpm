import datetime
from utils import knbrs, safe_ln
import networkx as nx


def fitness_function(seed_set, graph, propogation_probability):  # wolf,
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
        seed_set_item_neighbors = knbrs(graph, seed_set_item, 2)
        seed_set_with_neighbors[seed_set_item] = seed_set_item_neighbors
        s_prim += list(seed_set_item_neighbors)

    s_prim = set(s_prim)

    for node in set(s_prim):
        neighbors = knbrs(graph, node, 1)
        for neighbor in neighbors:
            edge_data = graph.get_edge_data(neighbor, node).get("days")
            # نحوه ارتباط برعکس در نظر گرفته شود -- بررسی نتیجه
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
