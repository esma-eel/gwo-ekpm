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


def test_5_3_2_astro_data():
    data = test_5_3_2_data_extraction(
        "/home/esmaeel/work/thesis/thesis_main/src"
        "/results/gwim/5.3.1.2/astro/gwim_default_5.3.1.2_out.json"
    )

    graph_data = test_5_3_2_graph_data(data)
    return graph_data


def test_5_3_2_ham_data():
    data = test_5_3_2_data_extraction(
        "/home/esmaeel/work/thesis/thesis_main/src"
        "/results/gwim/5.3.1.2/ham/gwim_default_ham_5.3.1.2_out.json"
    )

    graph_data = test_5_3_2_graph_data(data)
    return graph_data


def test_5_3_2_pgp_data():
    data = test_5_3_2_data_extraction(
        "/home/esmaeel/work/thesis/thesis_main/src"
        "/results/gwim/5.3.1.2/pgp/gwim_default_pgp_5.3.1.2_out.json"
    )

    graph_data = test_5_3_2_graph_data(data)
    return graph_data


test_5_3_2_astro = test_5_3_2_astro_data()
test_5_3_2_ham = test_5_3_2_ham_data()
test_5_3_2_pgp = test_5_3_2_pgp_data()

plt.plot(
    test_5_3_2_astro["prbs"],
    test_5_3_2_astro["influentiality"],
    label="AST",
)

plt.plot(
    test_5_3_2_ham["prbs"],
    test_5_3_2_ham["influentiality"],
    label="HAM",
)

plt.plot(
    test_5_3_2_pgp["prbs"],
    test_5_3_2_pgp["influentiality"],
    label="PGP",
)

plt.xlabel("Propogation Probability (PRB)")
plt.ylabel("Influentiality")
plt.title("Evaluation Influentiality [Propogation PRB] (GWIM)")
plt.legend()
plt.show()
