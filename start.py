#!/usr/bin/env python
"""
Esmaeel Komijani's Master Thesis Project (EKPM)
Created: 1402-03-08
Modified: 1402-03-23
"""

import argparse
import datetime

import numpy as np

from algorithms import gwolf
from cost_functions import (
    gwim_fitness_function,
    proposed_method_fitness_function,
)
from network import initial_graph

parser = argparse.ArgumentParser(
    description="EKPM (Esmaeel Komijani's Project Master)"
)

# cost function number
parser.add_argument(
    "-c",
    "--cost_function",
    metavar="Cname",
    type=int,
    required=False,
    default=1,
    help="Costfuncions List are [ 1)EKMP1 2)EKPM2 3)GWIM ]",
)

# seed set size
parser.add_argument(
    "-kstart",
    "--seed_set_size_start",
    metavar="K",
    type=int,
    required=True,
    help="Seed set size(k) start number",
)
parser.add_argument(
    "-kstop",
    "--seed_set_size_stop",
    metavar="K",
    type=int,
    required=False,
    help="Seed set size(k) stop number",
)
parser.add_argument(
    "-kstep",
    "--seed_set_size_step",
    metavar="K",
    type=int,
    required=False,
    help="Seed set size(k) step number",
)

# monte carlo simulation repeats
parser.add_argument(
    "-m",
    "--monte_carlo",
    metavar="M",
    type=int,
    required=True,
    help="Monte carlo simulation repeats",
)

# population size
parser.add_argument(
    "-ps",
    "--population_size",
    metavar="P",
    type=int,
    required=True,
    help="Population size of wolves",
)

# maximum iterations
parser.add_argument(
    "-t",
    "--max_t",
    metavar="T",
    type=int,
    required=True,
    help="Maximum iterations of gray wolf optimization algorithm",
)

# (v') v prim degree limit
parser.add_argument(
    "-vdl",
    "--v_prim_degree_limit",
    metavar="L",
    type=int,
    required=True,
    help=(
        "Least degree nodes can have in main graph in order to start alogrithm"
    ),
)

# propogation probability
parser.add_argument(
    "-ppstart",
    "--propogation_probability_start",
    metavar="P",
    type=float,
    required=True,
    default=0.02,
    help="Propogation probability to activate nodes start",
)
parser.add_argument(
    "-ppstop",
    "--propogation_probability_stop",
    metavar="P",
    type=float,
    required=False,
    help="Propogation probability to activate nodes stop",
)
parser.add_argument(
    "-ppstep",
    "--propogation_probability_step",
    metavar="P",
    type=float,
    required=False,
    help="Propogation probability to activate nodes start",
)

# impact range
parser.add_argument(
    "-i",
    "--impact_range",
    metavar="I",
    type=int,
    required=True,
    default=60,
    help="Impact range number",
)

# average movement activation
parser.add_argument(
    "-am",
    "--average_movement",
    metavar="A",
    type=int,
    required=False,
    default=0,
    help="Average movement activation",
)

# dataset address
parser.add_argument(
    "-d",
    "--dataset",
    metavar="Address",
    type=str,
    required=True,
    default="./dataset/CA-AstroPh3.tsv",
    help="Dataset file address",
)


args = parser.parse_args()

print(args.cost_function)
print(args.seed_set_size_start)
print(args)
print(vars(args))


def run_ekpm1(**paramters):
    gwolf_args = {
        **paramters,
        "reverse": False,
        "cost_function": proposed_method_fitness_function,
    }
    alogrithm_execution_result = gwolf(**gwolf_args)
    return alogrithm_execution_result


def run_ekpm2(**paramters):
    gwolf_args = {
        **paramters,
        "reverse": True,
        "cost_function": proposed_method_fitness_function,
    }
    alogrithm_execution_result = gwolf(**gwolf_args)
    return alogrithm_execution_result


def run_gwim(**paramters):
    gwolf_args = {
        **paramters,
        "cost_function": gwim_fitness_function,
    }
    alogrithm_execution_result = gwolf(**gwolf_args)
    return alogrithm_execution_result


def get_run_options():
    return {1: run_ekpm1, 2: run_ekpm2, 3: run_gwim}


def range_dict(**range_args):
    params = {"iterate": False, "parameter": "", "function": range(1)}

    kstart = range_args.get("seed_set_size_start")
    kstop = range_args.get("seed_set_size_stop")
    kstep = range_args.get("seed_set_size_step")

    if kstart and kstop and kstep:
        params["iterate"] = True
        params["parameter"] = "seed_set_size_start"
        params["function"] = range(kstart, kstop, kstep)
        return params

    ppstart = range_args.get("propogation_probability_start")
    ppstop = range_args.get("propogation_probability_stop")
    ppstep = range_args.get("propogation_probability_step")

    if ppstart and ppstop and ppstep:
        params["iterate"] = True
        params["parameter"] = "propogation_probability_start"
        params["function"] = np.linspace(ppstart, ppstop, ppstep)
        return params

    return params


def run(**run_args):
    graph = initial_graph(
        dataset_addres=run_args.get("dataset"),
        v_prim_degree_limit=run_args.get("v_prim_degree_limit"),
    )
    run_start_datetime = datetime.datetime.now()

    run_options = get_run_options()
    run_option_choice = run_args.get("cost_function")
    run_option = run_options[run_option_choice]

    range = range_dict(**run_args)
    parameters = {**run_args, "graph": graph}
    execute_history = []

    for counter in range.get("function"):
        iteration_start_datetiem = datetime.datetime.now()
        if range.get("iterate"):
            parameters[range.get("parameter")] = counter

        counter_result = run_option(**parameters)
        iteration_end_datetime = datetime.datetime.now()

        iteration_delta = iteration_end_datetime - iteration_start_datetiem

        history = {
            "action": "display_finished_algorithm",
            "time": str(iteration_delta),
            "params": parameters,
            "algorithm_result": counter_result,
        }
        if range.get("iterate"):
            history["changing_parameter"] = range.get("parameter")

        execute_history.append(history)
        print(history)

    run_end_dateitme = datetime.datetime.now()
    run_delta = run_end_dateitme - run_start_datetime

    print(
        {
            "action": "display_end_execution",
            "total": run_delta,
            "executions": execute_history,
        }
    )


if __name__ == "__main__":
    run_args = vars(args)
    run(**run_args)


"""
# defualt
python start.py -c 1 -kstart 40 -m 50 -ps 50 -t 100 -vdl 2 -ppstart 0.02 -i 60
 -d "./dataset/CA-AstroPH3.tsv"
"""
