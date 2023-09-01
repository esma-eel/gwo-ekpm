import datetime
from utils import knbrs, safe_ln
import networkx as nx
from utils import graph_nodes


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

    first_order_s = set()
    second_order_s = set()
    for node_of_s in seed_set:
        if node_of_s in first_order_neighbors:
            first_order_s.add(node_of_s)
        elif node_of_s in second_order_neighbors:
            second_order_s.add(node_of_s)

    for i in first_order_s:
        sum_first_order_neighbors += position[nodes_list.index(i)]

    for i in first_order_s:
        for k in second_order_s:
            k_neighbors = knbrs(graph, k, 1)
            if i in k_neighbors:
                sum_second_order_neighbors += (
                    position[nodes_list.index(i)]
                    * position[nodes_list.index(k)]
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


def gwim_default(**parameters):
    start = datetime.datetime.now()

    seed_set = parameters.get("seed_set")
    position = parameters.get("position")
    graph = parameters.get("graph")

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


def ekpm_full(**parameters):
    start = datetime.datetime.now()
    """
    calculating the fitness value for 'wolf'
    based on part 4.1 equation 13 in article
    """
    graph = parameters.get("graph")
    seed_set = parameters.get("seed_set")
    reverse = parameters.get("reverse")
    impact_range = parameters.get("impact_range")
    propogation_probability = parameters.get("propogation_probability_start")

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
            if reverse:
                if edge_data > impact_range and neighbor in s_prim:
                    s_prim.remove(neighbor)
            else:
                if edge_data < impact_range and neighbor in s_prim:
                    s_prim.remove(neighbor)

    if not s_prim:
        return 0

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


def ekpm_impact_range_gwim(**parameters):
    start = datetime.datetime.now()

    seed_set = parameters.get("seed_set")
    position = parameters.get("position")
    graph = parameters.get("graph")
    reverse = parameters.get("reverse")
    impact_range = parameters.get("impact_range")

    s_prim = []
    for seed_set_item in seed_set:
        seed_set_item_neighbors = knbrs(graph, seed_set_item, 2)
        s_prim += list(seed_set_item_neighbors)

    s_prim = set(s_prim)
    s_prim_graph = nx.Graph(graph.subgraph(s_prim))
    if reverse:
        keep_edges = list(
            filter(
                lambda e: e[2] < impact_range,
                (e for e in s_prim_graph.edges.data("days")),
            )
        )
    else:
        keep_edges = list(
            filter(
                lambda e: e[2] > impact_range,
                (e for e in s_prim_graph.edges.data("days")),
            )
        )

    s_prim_graph.clear()
    s_prim_graph.add_weighted_edges_from(keep_edges)

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


def ekpm_impact_range_eigv(**parameters):
    start = datetime.datetime.now()

    graph = parameters.get("graph")
    seed_set = parameters.get("seed_set")
    reverse = parameters.get("reverse")
    impact_range = parameters.get("impact_range")

    s_prim = []
    seed_set_with_neighbors = {}
    for seed_set_item in seed_set:
        seed_set_item_neighbors = knbrs(graph, seed_set_item, 2)
        seed_set_with_neighbors[seed_set_item] = seed_set_item_neighbors
        s_prim += list(seed_set_item_neighbors)

    s_prim = set(s_prim)

    if not s_prim:
        return 0

    s_prim_graph = nx.Graph(graph.subgraph(s_prim))
    if reverse:
        keep_edges = list(
            filter(
                lambda e: e[2] < impact_range,
                (e for e in s_prim_graph.edges.data("days")),
            )
        )
    else:
        keep_edges = list(
            filter(
                lambda e: e[2] > impact_range,
                (e for e in s_prim_graph.edges.data("days")),
            )
        )

    s_prim_graph.clear()
    s_prim_graph.add_weighted_edges_from(keep_edges)

    tolerance_range = 6
    s_prim_eigenvector = None
    while not s_prim_eigenvector:
        if tolerance_range >= 0:
            default_fault_tolerance = f"1.0e-{tolerance_range}"
        else:
            default_fault_tolerance = 1

        try:
            s_prim_eigenvector = nx.eigenvector_centrality(
                s_prim_graph,
                weight="days",
                tol=float(default_fault_tolerance),
            )
        except nx.PowerIterationFailedConvergence:
            tolerance_range -= 1

    s_prim_eigenvector = dict(
        sorted(
            s_prim_eigenvector.items(),
            reverse=True,
        )
    )
    s_prim_eigenvector_worthy = {}
    for (
        seed_set_item,
        seed_set_item_neighbors,
    ) in seed_set_with_neighbors.items():
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


def ekpm_impact_range_eigv_kshell_filter(**parameters):
    start = datetime.datetime.now()

    graph = parameters.get("graph")
    seed_set = parameters.get("seed_set")
    reverse = parameters.get("reverse")
    impact_range = parameters.get("impact_range")

    s_prim = []
    seed_set_with_neighbors = {}
    for seed_set_item in seed_set:
        seed_set_item_neighbors = knbrs(graph, seed_set_item, 2)
        seed_set_with_neighbors[seed_set_item] = seed_set_item_neighbors
        s_prim += list(seed_set_item_neighbors)

    s_prim = set(s_prim)

    if not s_prim:
        return 0

    s_prim_graph = nx.Graph(graph.subgraph(s_prim))
    if reverse:
        keep_edges = list(
            filter(
                lambda e: e[2] < impact_range,
                (e for e in s_prim_graph.edges.data("days")),
            )
        )
    else:
        keep_edges = list(
            filter(
                lambda e: e[2] > impact_range,
                (e for e in s_prim_graph.edges.data("days")),
            )
        )

    s_prim_graph.clear()
    s_prim_graph.add_weighted_edges_from(keep_edges)

    s_prim_sum_degrees = sum([degree for node, degree in s_prim_graph.degree()])
    s_prim_mean_degrees = s_prim_sum_degrees // len(s_prim)

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

    s_prim_eigenvector = dict(
        sorted(
            s_prim_eigenvector.items(),
            reverse=True,
        )
    )
    s_prim_eigenvector_worthy = {}
    for (
        seed_set_item,
        seed_set_item_neighbors,
    ) in seed_set_with_neighbors.items():
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


def ekpm_impact_range_eigv_prb_filter(**parameters):
    start = datetime.datetime.now()

    graph = parameters.get("graph")
    seed_set = parameters.get("seed_set")
    reverse = parameters.get("reverse")
    impact_range = parameters.get("impact_range")
    propogation_probability = parameters.get("propogation_probability_start")

    s_prim = []
    seed_set_with_neighbors = {}
    for seed_set_item in seed_set:
        seed_set_item_neighbors = knbrs(graph, seed_set_item, 2)
        seed_set_with_neighbors[seed_set_item] = seed_set_item_neighbors
        s_prim += list(seed_set_item_neighbors)

    s_prim = set(s_prim)

    if not s_prim:
        return 0

    s_prim_graph = nx.Graph(graph.subgraph(s_prim))
    if reverse:
        keep_edges = list(
            filter(
                lambda e: e[2] < impact_range,
                (e for e in s_prim_graph.edges.data("days")),
            )
        )
    else:
        keep_edges = list(
            filter(
                lambda e: e[2] > impact_range,
                (e for e in s_prim_graph.edges.data("days")),
            )
        )

    s_prim_graph.clear()
    s_prim_graph.add_weighted_edges_from(keep_edges)

    tolerance_range = 6
    s_prim_eigenvector = None
    while not s_prim_eigenvector:
        if tolerance_range >= 0:
            default_fault_tolerance = f"1.0e-{tolerance_range}"
        else:
            default_fault_tolerance = 1

        try:
            s_prim_eigenvector = nx.eigenvector_centrality(
                s_prim_graph,
                weight="days",
                tol=float(default_fault_tolerance),
            )
        except nx.PowerIterationFailedConvergence:
            tolerance_range -= 1

    s_prim_eigenvector = dict(
        sorted(
            s_prim_eigenvector.items(),
            key=lambda item: item[1] >= propogation_probability,
            reverse=True,
        )
    )
    s_prim_eigenvector_worthy = {}
    for (
        seed_set_item,
        seed_set_item_neighbors,
    ) in seed_set_with_neighbors.items():
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


def ekpm_impact_range_eigv_kshell_prb_filter(**parameters):
    start = datetime.datetime.now()

    graph = parameters.get("graph")
    seed_set = parameters.get("seed_set")
    reverse = parameters.get("reverse")
    impact_range = parameters.get("impact_range")
    propogation_probability = parameters.get("propogation_probability_start")

    s_prim = []
    seed_set_with_neighbors = {}
    for seed_set_item in seed_set:
        seed_set_item_neighbors = knbrs(graph, seed_set_item, 2)
        seed_set_with_neighbors[seed_set_item] = seed_set_item_neighbors
        s_prim += list(seed_set_item_neighbors)

    s_prim = set(s_prim)

    if not s_prim:
        return 0

    s_prim_graph = nx.Graph(graph.subgraph(s_prim))
    if reverse:
        keep_edges = list(
            filter(
                lambda e: e[2] < impact_range,
                (e for e in s_prim_graph.edges.data("days")),
            )
        )
    else:
        keep_edges = list(
            filter(
                lambda e: e[2] > impact_range,
                (e for e in s_prim_graph.edges.data("days")),
            )
        )

    s_prim_graph.clear()
    s_prim_graph.add_weighted_edges_from(keep_edges)

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

    s_prim_eigenvector = dict(
        sorted(
            s_prim_eigenvector.items(),
            key=lambda item: item[1] >= propogation_probability,
            reverse=True,
        )
    )
    s_prim_eigenvector_worthy = {}
    for (
        seed_set_item,
        seed_set_item_neighbors,
    ) in seed_set_with_neighbors.items():
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
