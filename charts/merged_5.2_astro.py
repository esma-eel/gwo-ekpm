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

    avg_history_raw_data = data["executions"][0]["algorithm_result"][
        "average_movement_history"
    ]
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


def test_5_2_gwim_data():
    data = test_5_2_data_extraction(
        "/home/esmaeel/work/thesis/thesis_main/src"
        "/results/gwim/5.2/gwim_asto.json"
    )

    graph_data = test_5_2_graph_data(data, 0, 17, 0, 10)
    return graph_data


def test_5_2_ekpm_s1_data():
    data = test_5_2_data_extraction(
        "/home/esmaeel/work/thesis/thesis_main/src"
        "/results/ekpm/5.2/s1/ekpm_s1_astro.json"
    )

    graph_data = test_5_2_graph_data(data, 0, 19, 0, 10)
    return graph_data


def test_5_2_ekpm_s2_data():
    data = test_5_2_data_extraction(
        "/home/esmaeel/work/thesis/thesis_main/src"
        "/results/ekpm/5.2/s2/ekpm_s2_astro.json"
    )

    graph_data = test_5_2_graph_data(data, 0, 17, 0, 10)
    return graph_data


test_5_2_gwim = test_5_2_gwim_data()
test_5_2_ekpm1 = test_5_2_ekpm_s1_data()
test_5_2_ekpm2 = test_5_2_ekpm_s2_data()

plt.plot(
    test_5_2_gwim["iterations"],
    test_5_2_gwim["average_movements"],
    label="GWIM",
)

plt.plot(
    test_5_2_ekpm1["iterations"],
    test_5_2_ekpm1["average_movements"],
    label="EKPM S1",
)

plt.plot(
    test_5_2_ekpm2["iterations"],
    test_5_2_ekpm2["average_movements"],
    label="EKPM S2",
)

plt.xlabel("Iterations")
plt.ylabel("AM")
plt.title("Convergence Speed (ASTRO)")
plt.legend()
plt.show()
