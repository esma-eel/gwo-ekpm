"""
import datetime
import copy

# import numpy as np

from constants import (
    MAX_T,
    POPULATION_SIZE,
    SEED_SET_SIZE,
    MONTE_CARLO_SIMULATION_NUMBER,
    PROPOGATION_PROBABILITY,
    AVERAGE_MOVEMENT,
)
from cost_functions import ekpm_full as fitness_function
from independent_cascade import independent_cascade_simulation
from wolf import Wolf
from network import initial_graph

if AVERAGE_MOVEMENT:
    from utils import calculate_average_movement

graph = initial_graph()


if __name__ == "__main__":
    whole_process_start = datetime.datetime.now()
    reverse = False
    parameters = {
        "SEED_SET_SIZE": SEED_SET_SIZE,
        "MONTE_CARLO_SIMULATION_NUMBER": MONTE_CARLO_SIMULATION_NUMBER,
        "POPULATION_SIZE": POPULATION_SIZE,
        "PROPOGATION_PROBABILITY": PROPOGATION_PROBABILITY,
        "MAX_T": MAX_T,
        "REVERSE": reverse,
    }

    execute_history = []
    test_parameters = {
        "parameter": "SEED_SET_SIZE",
        "AKA": "K",
        "start": 10,
        "end": 90,
        "step": 10,
        # "num": 1,
    }

    print("---TEST 5.3.1.1 --")
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
        execute_parameters[test_parameters["parameter"]] = counter0
        print(execute_parameters)
        start_main = datetime.datetime.now()
        algorithm_result = main(**execute_parameters)
        end_main = datetime.datetime.now()
        delta_main = end_main - start_main
        history = {
            "action": "display_finished_algorithm",
            "time": str(delta_main),
            test_parameters["AKA"]: counter0,
            "algorithm_result": algorithm_result,
        }
        execute_history.append(history)
        print(history)

    print(execute_history)
    whole_process_end = datetime.datetime.now()
    delta_process = whole_process_end - whole_process_start
    print("execution took: ", str(delta_process))
"""
