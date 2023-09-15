import networkx as nx


def initial_graph(dataset_addres, v_prim_degree_limit):
    """
    create graph based on dataset address and the limit of nodes degree
    based on main article ==> default is 1
    """
    graph_type = nx.Graph()
    G = nx.read_edgelist(
        dataset_addres,
        create_using=graph_type,
        data=(("days", int),),
        nodetype=int,
    )

    # placeholder for nodes with degree >= V_PRIM_DEGREE_LIMIT
    v_prim_nodes = []

    # create new graph with nodes which degree >= V_PRIM_DEGREE_LIMIT
    for node in G:
        if G.degree(node) >= v_prim_degree_limit:
            v_prim_nodes.append(node)

    V_PRIM_GRAPH = G.subgraph(v_prim_nodes)
    V_PRIM_GRAPH = nx.Graph(V_PRIM_GRAPH)
    V_PRIM_GRAPH.remove_edges_from(list(nx.selfloop_edges(V_PRIM_GRAPH)))

    return V_PRIM_GRAPH
