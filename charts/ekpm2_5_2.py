import json
import os
import sys

import matplotlib.pyplot as plt

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)


from utils import remap


def test_5_2_data_extraction(file_address):
    data = {}
    with open(file_address, "r") as json_file:
        data = json.load(json_file)

    avg_history_raw_data = data["algorithm_result"]["average_movement_history"]
    return avg_history_raw_data


def test_5_2_graph_data(data, omin=0, omax=1000, nmin=0, nmax=10):
    average_movements = []
    iterations = []

    for item in data:
        iterations.append(item["iteration"])
        value = item["value"]
        value = remap(value, omin, omax, nmin, nmax)
        average_movements.append(value)

    return {"average_movements": average_movements, "iterations": iterations}


def test_5_2_astro_data():
    data = test_5_2_data_extraction(
        "/home/esmaeel/work/thesis/thesis_main/src"
        "/results/ekpm2/5.2/astro/ekpm2_5.2_astro.json"
    )

    graph_data = test_5_2_graph_data(data, 0, 61, 0, 10)
    return graph_data


def test_5_2_ham_data():
    data = test_5_2_data_extraction(
        "/home/esmaeel/work/thesis/thesis_main/src"
        "/results/ekpm2/5.2/ham/ekpm2_5.2_ham.json"
    )

    graph_data = test_5_2_graph_data(data, 0, 16, 0, 10)
    return graph_data


def test_5_2_pgp_data():
    data = test_5_2_data_extraction(
        "/home/esmaeel/work/thesis/thesis_main/src"
        "/results/ekpm2/5.2/pgp/ekpm2_5.2_pgp.json"
    )

    graph_data = test_5_2_graph_data(data, 0, 30, 0, 10)
    return graph_data


test_5_2_astro = test_5_2_astro_data()
test_5_2_ham = test_5_2_ham_data()
test_5_2_pgp = test_5_2_pgp_data()

plt.plot(
    test_5_2_astro["iterations"],
    test_5_2_astro["average_movements"],
    label="AST",
)

plt.plot(
    test_5_2_ham["iterations"],
    test_5_2_ham["average_movements"],
    label="HAM",
)

plt.plot(
    test_5_2_pgp["iterations"],
    test_5_2_pgp["average_movements"],
    label="PGP",
)

plt.xlabel("Iterations")
plt.ylabel("AM")
plt.title("Convergence Speed (EKPM 2)")
plt.legend()
plt.show()
