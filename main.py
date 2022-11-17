import datetime
import copy

# import numpy as np

from constants import (
    MAX_T,
    POPULATION_SIZE,
    SEED_SET_SIZE,
    MONTE_CARLO_SIMULATION_NUMBER,
    PROPOGATION_PROBABILITY,
)
from cost_functions import fitness_function
from independent_cascade import independent_cascade_simulation

from utils import calculate_average_movement
from wolf import Wolf
from network import initial_graph

graph = initial_graph()


def main(
    SEED_SET_SIZE,
    MONTE_CARLO_SIMULATION_NUMBER,
    POPULATION_SIZE,
    PROPOGATION_PROBABILITY,
    MAX_T,
):
    """
    main function of gwim algorithm and running independent cascade for
    alpha wolf seed set
    """

    alpha_history = []
    # iteration counter
    iteration = 0  # iteration 0 is starter iteration
    print({"iteration": iteration, "action": "generate_population"})
    population = [Wolf() for _ in range(POPULATION_SIZE)]

    for wolf in population:
        print(
            {
                "iteration": iteration,
                "action": "generate_position",
                "wolf": wolf.id,
            }
        )

        wolf.random_position(graph=graph)
        print(
            {
                "iteration": iteration,
                "action": "generate_seed_set",
                "wolf": wolf.id,
            }
        )
        wolf.generate_corresponding_seed_set(
            graph=graph, SEED_SET_SIZE=SEED_SET_SIZE
        )
        print(
            {
                "iteration": iteration,
                "action": "display_seed_set",
                "wolf": wolf.id,
                "seed_set": hash(tuple(wolf.S)),
            }
        )
        print(
            {
                "iteration": iteration,
                "action": "calculate_fitness",
                "wolf": wolf.id,
            }
        )
        fitness_value = fitness_function(
            seed_set=wolf.S,
            graph=graph,
            propogation_probability=PROPOGATION_PROBABILITY,
        )
        wolf.value = fitness_value
        print({"iteration": iteration, "wolf": wolf.id, "value": wolf.value})

    print(
        {
            "iteration": iteration,
            "action": "extract_top_wolves",
        }
    )
    population = sorted(
        population,
        key=lambda wolf: wolf.value,
        reverse=True,
    )
    alpha, beta, delta = copy.copy(population[:3])
    print(
        {
            "iteration": iteration,
            "action": "display_top_wolves",
            "alpha": {
                "wolf": alpha.id,
                "value": alpha.value,
                "seed_set": hash(tuple(alpha.S)),
                "position": hash(tuple(alpha.X)),
            },
            "beta": {
                "wolf": beta.id,
                "value": beta.value,
                "seed_set": hash(tuple(beta.S)),
                "position": hash(tuple(beta.X.values())),
            },
            "delta": {
                "wolf": delta.id,
                "value": delta.value,
                "seed_set": hash(tuple(delta.S)),
                "position": hash(tuple(delta.X.values())),
            },
        }
    )

    # keep history of alphas before main iterations
    if alpha not in alpha_history:
        alpha_history.append(
            {
                "iteration": iteration,
                "action": "register_alpha_history",
                "wolf": alpha.id,
                "value": alpha.value,
                "seed_set": hash(tuple(alpha.S)),
                "position": hash(tuple(alpha.X.values())),
            }
        )

    # omega_wolves = population_sorted[3:]

    for iteration in range(1, MAX_T + 1, 1):
        print(f"---------- iteration {iteration} -----------")
        for wolf in population:
            print(
                {
                    "iteration": iteration,
                    "action": "update_position",
                    "wolf": wolf.id,
                }
            )
            wolf.update_position(
                alpha=alpha,
                beta=beta,
                delta=delta,
                iteration=iteration,
                graph=graph,
                MAX_T=MAX_T,
            )
            print(
                {
                    "iteration": iteration,
                    "action": "update_seed_set",
                    "wolf": wolf.id,
                }
            )
            wolf.generate_corresponding_seed_set(
                graph=graph,
                SEED_SET_SIZE=SEED_SET_SIZE,
            )
            print(
                {
                    "iteration": iteration,
                    "action": "display_seed_set",
                    "wolf": wolf.id,
                    "seed_set": hash(tuple(wolf.S)),
                }
            )

        for wolf in population:
            print(
                {
                    "iteration": iteration,
                    "action": "calculate_fitness",
                    "wolf": wolf.id,
                }
            )
            fitness_value = fitness_function(
                seed_set=wolf.S,
                graph=graph,
                propogation_probability=PROPOGATION_PROBABILITY,
            )
            wolf.value = fitness_value
            print(
                {
                    "iteration": iteration,
                    "action": "display_value",
                    "wolf": wolf.id,
                    "value": wolf.value,
                }
            )

        print(
            {
                "iteration": iteration,
                "action": "extract_top_wolves",
            }
        )
        population = sorted(
            population,
            key=lambda wolf: wolf.value,
            reverse=True,
        )
        alpha, beta, delta = copy.copy(population[:3])
        print(
            {
                "iteration": iteration,
                "action": "display_top_wolves",
                "alpha": {
                    "wolf": alpha.id,
                    "value": alpha.value,
                    "seed_set": hash(tuple(alpha.S)),
                    "position": hash(tuple(alpha.X)),
                },
                "beta": {
                    "wolf": beta.id,
                    "value": beta.value,
                    "seed_set": hash(tuple(beta.S)),
                    "position": hash(tuple(beta.X.values())),
                },
                "delta": {
                    "wolf": delta.id,
                    "value": delta.value,
                    "seed_set": hash(tuple(delta.S)),
                    "position": hash(tuple(delta.X.values())),
                },
            }
        )

        # keep history of alphas during iterations
        if alpha not in alpha_history:
            alpha_history.append(
                {
                    "iteration": iteration,
                    "action": "register_alpha_history",
                    "wolf": alpha.id,
                    "value": alpha.value,
                    "seed_set": hash(tuple(alpha.S)),
                    "position": hash(tuple(alpha.X.values())),
                }
            )

        # omega_wolves = population_sorted[3:]
        if (beta.X.values() == alpha.X.values()) or (
            delta.X.values() == beta.X.values()
        ):
            print(
                {
                    "iteration": iteration,
                    "action": "regenerate_beta_position",
                    "wolf": beta.id,
                }
            )
            beta.random_position(graph=graph)
            beta.register_position_history(iteration)

            print(
                {
                    "iteration": iteration,
                    "action": "regenerate_delta_position",
                    "wolf": delta.id,
                }
            )
            delta.random_position(graph=graph)
            delta.register_position_history(iteration)

        average_movement = calculate_average_movement(
            population, iteration - 1, iteration
        )
        print(
            {
                "iteration": iteration,
                "action": "display_average_movement",
                "for": str((iteration - 1, iteration)),
                "value": average_movement,
            }
        )
    # end iteration

    print({"action": "display_population", "status": "final"})
    for wolf in population:
        print(
            {
                "wolf": wolf.id,
                "value": wolf.value,
                "seed_set": hash(tuple(wolf.S)),
                "position": hash(tuple(wolf.X.values())),
            }
        )

    print({"action": "display_alpha", "status": "final"})
    print(
        alpha,
        alpha.value,
        alpha.S,
    )

    print({"action": "display_alpha_history"})
    for u_alpha in alpha_history:
        print(u_alpha)

    print({"action": "run_ic_simulation"})
    independent_cascade_result = independent_cascade_simulation(
        seed_set=alpha.S,
        graph=graph,
        PROPOGATION_PROBABILITY=PROPOGATION_PROBABILITY,
        MONTE_CARLO_SIMULATION_NUMBER=MONTE_CARLO_SIMULATION_NUMBER,
    )

    print({"action": "display_ic_result"})
    print(independent_cascade_result)

    return {
        "ic": independent_cascade_result,
        "network_size": len(graph.nodes()),
        "alpha": {
            "wolf": alpha.id,
            "position": hash(tuple(alpha.X.values())),
            "seed_set": alpha.S,
        },
    }


if __name__ == "__main__":
    whole_process_start = datetime.datetime.now()
    parameters = {
        "SEED_SET_SIZE": SEED_SET_SIZE,
        "MONTE_CARLO_SIMULATION_NUMBER": MONTE_CARLO_SIMULATION_NUMBER,
        "POPULATION_SIZE": POPULATION_SIZE,
        "PROPOGATION_PROBABILITY": PROPOGATION_PROBABILITY,
        "MAX_T": MAX_T,
    }

    execute_history = []
    test_parameters = {
        # "parameter": "PROPOGATION_PROBABILITY",
        # "AKA": "P",
        "start": 1,
        "end": 2,
        "step": 1,
        # "num": 1,
    }

    print("---TEST 5.2--")
    print({"action": "display_test_paramters", "test": test_parameters})
    # for counter0 in np.linspace(
    #     test_parameters["start"],
    #     test_parameters["end"],
    #     test_parameters["num"],
    # ):
    for counter0 in range(
        test_parameters["start"],
        test_parameters["end"],
        test_parameters["step"],
    ):
        execute_parameters = {
            **parameters,
        }
        # execute_parameters[test_parameters["parameter"]] = counter0
        print(execute_parameters)
        start_main = datetime.datetime.now()
        algorithm_result = main(**execute_parameters)
        end_main = datetime.datetime.now()
        delta_main = end_main - start_main
        history = {
            "action": "display_finished_algorithm",
            "time": str(delta_main),
            # test_parameters["AKA"]: counter0,
            "algorithm_result": algorithm_result,
        }
        execute_history.append(history)
        print(history)

    print(execute_history)
    whole_process_end = datetime.datetime.now()
    delta_process = whole_process_end - whole_process_start
    print("execution took: ", str(delta_process))
