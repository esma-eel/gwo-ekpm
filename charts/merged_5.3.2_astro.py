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


def test_5_3_2_data_extraction(file_address):
    data = {}
    with open(file_address, "r") as json_file:
        data = json.load(json_file)

    executions = data["executions"]
    raw_data = []
    for execution in executions:
        prb = execution["params"]["propogation_probability_start"]
        ic = execution["algorithm_result"]["ic"]
        network_size = execution["algorithm_result"]["network_size"]

        raw_data.append(
            {
                "prb": prb,
                "ic": ic,
                "network_size": network_size,
            }
        )

    return raw_data


def test_5_3_2_graph_data(data):
    prbs = []
    influentiality = []

    for item in data:
        prbs.append(item.get("prb"))
        influence = float(item["ic"]) / float(item["network_size"])
        influentiality.append(influence)

    return {"prbs": prbs, "influentiality": influentiality}


def test_5_3_2_gwim_data():
    data = test_5_3_2_data_extraction(
        "/home/esmaeel/work/thesis/thesis_main/src"
        "/results/gwim/5.3.1.2/astro/gwim_default_5.3.1.2_out.json"
    )

    graph_data = test_5_3_2_graph_data(data)
    return graph_data


def test_5_3_2_ekpm_s1_data():
    data = test_5_3_2_data_extraction(
        "/home/esmaeel/work/thesis/thesis_main/src"
        "/results/ekpm/5.3.1.2/astro/ekpm_5.3.2_s1_astro.json"
    )

    graph_data = test_5_3_2_graph_data(data)
    return graph_data


def test_5_3_2_ekpm_s2_data():
    data = test_5_3_2_data_extraction(
        "/home/esmaeel/work/thesis/thesis_main/src"
        "/results/ekpm/5.3.1.2/astro/ekpm_5.3.2_s2_astro.json"
    )

    graph_data = test_5_3_2_graph_data(data)
    return graph_data


test_5_3_2_gwim = test_5_3_2_gwim_data()
test_5_3_2_ekpm_s1 = test_5_3_2_ekpm_s1_data()
test_5_3_2_ekpm_s2 = test_5_3_2_ekpm_s2_data()

plt.plot(
    test_5_3_2_gwim["prbs"],
    test_5_3_2_gwim["influentiality"],
    label="GWIM",
)

plt.plot(
    test_5_3_2_ekpm_s1["prbs"],
    test_5_3_2_ekpm_s1["influentiality"],
    label="EKPM S1",
)

plt.plot(
    test_5_3_2_ekpm_s2["prbs"],
    test_5_3_2_ekpm_s2["influentiality"],
    label="EKPM S2",
)


plt.xlabel("Propogation Probability (PRB)")
plt.ylabel("Influentiality")
plt.title("Evaluation Influentiality [Propogation PRB] (ASTRO)")
plt.legend()
plt.show()
