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


def test_5_3_1_data_extraction(file_address):
    data = {}
    with open(file_address, "r") as json_file:
        data = json.load(json_file)

    executions = data["executions"]
    raw_data = []
    for execution in executions:
        seed_set_size = execution["params"]["seed_set_size_start"]
        ic = execution["algorithm_result"]["ic"]
        network_size = execution["algorithm_result"]["network_size"]

        raw_data.append(
            {
                "seed_set_size": seed_set_size,
                "ic": ic,
                "network_size": network_size,
            }
        )

    return raw_data


def test_5_3_1_graph_data(data):
    seed_set_sizes = []
    influentiality = []

    for item in data:
        seed_set_sizes.append(item.get("seed_set_size"))
        influence = float(item["ic"]) / float(item["network_size"])
        influentiality.append(influence)

    return {"seed_set_sizes": seed_set_sizes, "influentiality": influentiality}


def test_5_3_1_gwim_data():
    data = test_5_3_1_data_extraction(
        "/home/esmaeel/work/thesis/thesis_main/src"
        "/results/gwim/5.3.1.1/ham/gwim_default_ham_5.3.1.1_out.json"
    )

    graph_data = test_5_3_1_graph_data(data)
    return graph_data


def test_5_3_1_ekpm_s1_data():
    data = test_5_3_1_data_extraction(
        "/home/esmaeel/work/thesis/thesis_main/src"
        "/results/ekpm/5.3.1.1/ham/ekpm_5.3.1_s1_ham.json"
    )

    graph_data = test_5_3_1_graph_data(data)
    return graph_data


def test_5_3_1_ekpm_s2_data():
    data = test_5_3_1_data_extraction(
        "/home/esmaeel/work/thesis/thesis_main/src"
        "/results/ekpm/5.3.1.1/ham/ekpm_5.3.1_s2.json"
    )

    graph_data = test_5_3_1_graph_data(data)
    return graph_data


test_5_3_1_gwim = test_5_3_1_gwim_data()
test_5_3_1_ekpm_s1 = test_5_3_1_ekpm_s1_data()
test_5_3_1_ekpm_s2 = test_5_3_1_ekpm_s2_data()

plt.plot(
    test_5_3_1_gwim["seed_set_sizes"],
    test_5_3_1_gwim["influentiality"],
    label="GWIM",
)

plt.plot(
    test_5_3_1_ekpm_s1["seed_set_sizes"],
    test_5_3_1_ekpm_s1["influentiality"],
    label="EKPM S1",
)

plt.plot(
    test_5_3_1_ekpm_s2["seed_set_sizes"],
    test_5_3_1_ekpm_s2["influentiality"],
    label="EKPM S2",
)

plt.xlabel("Seed Set Sizes (K)")
plt.ylabel("Influentiality")
plt.title("Evaluation Influentiality [Seed Set Size] (HAM)")
plt.legend()
plt.show()
