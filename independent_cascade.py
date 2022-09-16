from constants import (
    PROPOGATION_PROBABILITY,
    MONTE_CARLO_SIMULATION_NUMBER,
)
import numpy as np


def independent_cascade_simulation(
    seed_set, graph
):
    """
    Input:  graph object, set of seed nodes, propagation probability
            and the number of Monte-Carlo simulations
    Output: average number of nodes influenced by the seed nodes
    """

    # Loop over the Monte-Carlo Simulations
    spread = []
    for i in range(MONTE_CARLO_SIMULATION_NUMBER):
        print(
            f"running simulation number {i} "
            f"from {MONTE_CARLO_SIMULATION_NUMBER}"
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
                        0, 1, len(list(graph.neighbors(node)))
                    )
                    < PROPOGATION_PROBABILITY
                )

                array_of_neighbors = np.array(
                    list(graph.neighbors(node))
                )
                new_ones += list(np.extract(success, array_of_neighbors))

            new_active = list(set(new_ones) - set(all_activated_nodes))

            # Add newly activated nodes to the set of activated nodes
            all_activated_nodes += new_active

        spread.append(len(all_activated_nodes))

    return np.mean(spread)
