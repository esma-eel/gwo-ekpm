import math


def safe_ln(value):
    """
    function to calculate natural log of value more safe
    """

    if value <= 0:
        return 0

    return math.log(value)


def graph_nodes(target_graph):
    nodes = list(target_graph.nodes())
    return nodes


def maximum_degree(target_graph):
    """
    calculating the maximum degree in graph
    to use in random position function
    """
    degree_sequence = sorted(
        (d for n, d in target_graph.degree()), reverse=True
    )
    dmax = max(degree_sequence)
    return dmax


def graph_length(target_graph):
    length: int = len(graph_nodes(target_graph))
    return length


def knbrs(G, start, k):
    nbrs = set([start])
    for _ in range(k):
        nbrs = set((nbr for n in nbrs for nbr in G[n]))

    # In order to prevent any recursion we remove node it self from neighbors
    if start in nbrs:
        nbrs.remove(start)
    return nbrs


def calculate_average_movement(wolves, prev_t, current_t):
    sum_movement = sum([wolf.move(prev_t, current_t) for wolf in wolves])
    return sum_movement / len(wolves)


def convert_positions_data(data):
    new_data = {}
    for key, value in data.items():
        print("for ", key, value)
        if type(value) == dict:
            print("in if ", key)
            new_data[int(key)] = convert_positions_data(value)
        else:
            print("in else ", key)
            print("type key ", type(key))
            print(int(key))
            print(" value ", value)
            print("type value: ", type(value))
            print(float(value))
            new_data[int(key)] = float(value)

    return new_data
