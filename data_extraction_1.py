import ast
import re


def load_data(file_name):
    with open(file_name, "r") as ofile:
        data = ofile.readlines()

    cleaned_data = []
    for line in data:
        changed_line = line.replace("'", '"')
        changed_line = line.replace("\n", "")

        if line.startswith("{"):
            # to remove graph class or anything likethat
            pattern = r"<.*?>"
            changed_line = re.sub(pattern, "None", changed_line)

            # to convert to dict
            changed_line = ast.literal_eval(changed_line)

        cleaned_data.append(changed_line)

    return cleaned_data


def find_actions(list, action_name):
    results = []
    for data in list:
        if type(data) == str:
            continue

        if data.get("action") == action_name:
            results.append(data)

    return results


def find_calculate_fitness_actions(list):
    results = find_actions(list, "calculate_fitness")
    iterations = []
    for index, item in enumerate(results):
        if item.get("iteration"):
            new_data = {**item, **results[index + 1]}
            iterations.append(new_data)

    return iterations


def extract_calculate_fitness_time(cleaned_data):
    cf_results = find_calculate_fitness_actions(cleaned_data)
    times_list = []
    for item in cf_results:
        times_list.append(item.get("time"))

    return {"fitness_time": {"min": min(times_list), "max": max(times_list)}}


def extract_alpha_values(cleaned_data):
    alpha_histories = find_actions(cleaned_data, "register_alpha_history")
    alpha_values = []
    for item in alpha_histories:
        value = item.get("value")
        alpha_values.append(value)

    return {
        "alpha_values": {
            "min": round(min(alpha_values), 4),
            "max": round(max(alpha_values), 4),
        }
    }


def extract_execution_metadata(cleaned_data):
    finished_algorithm = find_actions(
        cleaned_data, "display_finished_algorithm"
    )[0]
    algorithm_result = finished_algorithm["algorithm_result"]

    network_size = algorithm_result["network_size"]
    ic = algorithm_result["ic"]

    influence = ic / network_size
    influence = round(influence, 4)

    return {
        "time": finished_algorithm["time"],
        "network_size": network_size,
        "ic": ic,
        "influence": influence,
    }


def extract(file_name):
    file_data = load_data(file_name)
    calculate_fitness = extract_calculate_fitness_time(file_data)
    alpha_values = extract_alpha_values(file_data)
    metada = extract_execution_metadata(file_data)

    return {
        **metada,
        **calculate_fitness,
        **alpha_values,
    }


ham = [
    "results/ekpm/ekpm_ir_gwim_s1/ekpm_ir_gwim_s1_ham.txt",
    "results/ekpm/ekpm_ir_gwim_s2/ekpm_ir_gwim_s2_ham.txt",
    "results/ekpm/ekpm_ir_eigv_kshell_prb_s1/ekpm_ir_eigv_kshell_prb_s1_ham.txt",
    "results/ekpm/ekpm_ir_eigv_kshell_prb_s2/ekpm_ir_eigv_kshell_prb_s2_ham.txt",
    "results/ekpm/ekpm_ir_eigv_kshell_s1/ekpm_ir_eigv_kshell_s1_ham.txt",
    "results/ekpm/ekpm_ir_eigv_kshell_s2/ekpm_ir_eigv_kshell_s2_ham.txt",
    "results/ekpm/ekpm_ir_eigv_prb_s1/ekpm_ir_eigv_prb_s1_ham.txt",
    "results/ekpm/ekpm_ir_eigv_prb_s2/ekpm_ir_eigv_prb_s2_ham.txt",
    "results/ekpm/ekpm_ir_eigv_s1/ekpm_ir_eigv_s1_ham.txt",
    "results/ekpm/ekpm_ir_eigv_s2/ekpm_ir_eigv_s2_ham.txt",
    "results/ekpm/normal_s1/ekpm_default_s1_ham.txt",
    "results/ekpm/normal_s2/ekpm_default_s2_ham.txt",
    "results/gwim/normal/gwim_default_normal_test_ham.txt",
]
pgp = [
    "results/ekpm/ekpm_ir_gwim_s1/ekpm_ir_gwim_s1_pgp.txt",
    "results/ekpm/ekpm_ir_gwim_s2/ekpm_ir_gwim_s2_pgp.txt",
    "results/ekpm/ekpm_ir_eigv_kshell_prb_s1/ekpm_ir_eigv_kshell_prb_s1_pgp.txt",
    "results/ekpm/ekpm_ir_eigv_kshell_prb_s2/ekpm_ir_eigv_kshell_prb_s2_pgp.txt",
    "results/ekpm/ekpm_ir_eigv_kshell_s1/ekpm_ir_eigv_kshell_s1_pgp.txt",
    "results/ekpm/ekpm_ir_eigv_kshell_s2/ekpm_ir_eigv_kshell_s2_pgp.txt",
    "results/ekpm/ekpm_ir_eigv_prb_s1/ekpm_ir_eigv_prb_s1_pgp.txt",
    "results/ekpm/ekpm_ir_eigv_prb_s2/ekpm_ir_eigv_prb_s2_pgp.txt",
    "results/ekpm/ekpm_ir_eigv_s1/ekpm_ir_eigv_s1_pgp.txt",
    "results/ekpm/ekpm_ir_eigv_s2/ekpm_ir_eigv_s2_pgp.txt",
    "results/ekpm/normal_s1/ekpm_default_s1_pgp.txt",
    "results/ekpm/normal_s2/ekpm_default_s2_pgp.txt",
    "results/gwim/normal/gwim_default_normal_test_pgp.txt",
]

astro = [
    "results/ekpm/ekpm_ir_gwim_s1/ekpm_ir_gwim_s1.txt",
    "results/ekpm/ekpm_ir_gwim_s2/ekpm_ir_gwim_s2.txt",
    "results/ekpm/ekpm_ir_eigv_kshell_prb_s1/ekpm_ir_eigv_kshell_prb_s1.txt",
    "results/ekpm/ekpm_ir_eigv_kshell_prb_s2/ekpm_ir_eigv_kshell_prb_s2.txt",
    "results/ekpm/ekpm_ir_eigv_kshell_s1/ekpm_ir_eigv_kshell_s1.txt",
    "results/ekpm/ekpm_ir_eigv_kshell_s2/ekpm_ir_eigv_kshell_s2.txt",
    "results/ekpm/ekpm_ir_eigv_prb_s1/ekpm_ir_eigv_prb_s1.txt",
    "results/ekpm/ekpm_ir_eigv_prb_s2/ekpm_ir_eigv_prb_s2.txt",
    "results/ekpm/ekpm_ir_eigv_s1/ekpm_ir_eigv_s1.txt",
    "results/ekpm/ekpm_ir_eigv_s2/ekpm_ir_eigv_s2.txt",
    "results/ekpm/normal_s1/ekpm_default_s1.txt",
    "results/ekpm/normal_s2/ekpm_default_s2.txt",
    "results/gwim/normal/gwim_default_normal_test.txt",
]


extracted_data_ham = []

print("# // extracting HAM dataset...")
for file_name in ham:
    result = extract(file_name)
    extracted_data_ham.append({file_name: result})

print(extracted_data_ham)

extracted_data_pgp = []
print("# // extracting PGP dataset...")
for file_name in pgp:
    result = extract(file_name)
    extracted_data_pgp.append({file_name: result})

print(extracted_data_pgp)

extracted_data = []
print("# // extracting ASTRO dataset...")
for file_name in astro:
    result = extract(file_name)
    extracted_data.append({file_name: result})

print(extracted_data)


"""
ham
[
"results/ekpm/ekpm_ir_gwim_s1/ekpm_ir_gwim_s1_ham.txt",
"results/ekpm/ekpm_ir_gwim_s2/ekpm_ir_gwim_s2_ham.txt",
"results/ekpm/ekpm_ir_eigv_kshell_prb_s1/ekpm_ir_eigv_kshell_prb_s1_ham.txt",
"results/ekpm/ekpm_ir_eigv_kshell_prb_s2/ekpm_ir_eigv_kshell_prb_s2_ham.txt",
"results/ekpm/ekpm_ir_eigv_kshell_s1/ekpm_ir_eigv_kshell_s1_ham.txt",
"results/ekpm/ekpm_ir_eigv_kshell_s2/ekpm_ir_eigv_kshell_s2_ham.txt",
"results/ekpm/ekpm_ir_eigv_prb_s1/ekpm_ir_eigv_prb_s1_ham.txt",
"results/ekpm/ekpm_ir_eigv_prb_s2/ekpm_ir_eigv_prb_s2_ham.txt",
"results/ekpm/ekpm_ir_eigv_s1/ekpm_ir_eigv_s1_ham.txt",
"results/ekpm/ekpm_ir_eigv_s2/ekpm_ir_eigv_s2_ham.txt",
"results/ekpm/normal_s1/ekpm_default_s1_ham.txt",
"results/ekpm/normal_s2/ekpm_default_s2_ham.txt",
"results/gwim/normal/gwim_default_normal_test_ham.txt",

]

pgp
[
"results/ekpm/ekpm_ir_gwim_s1/ekpm_ir_gwim_s1_pgp.txt",
"results/ekpm/ekpm_ir_gwim_s2/ekpm_ir_gwim_s2_pgp.txt",
"results/ekpm/ekpm_ir_eigv_kshell_prb_s1/ekpm_ir_eigv_kshell_prb_s1_pgp.txt",
"results/ekpm/ekpm_ir_eigv_kshell_prb_s2/ekpm_ir_eigv_kshell_prb_s2_pgp.txt",
"results/ekpm/ekpm_ir_eigv_kshell_s1/ekpm_ir_eigv_kshell_s1_pgp.txt",
"results/ekpm/ekpm_ir_eigv_kshell_s2/ekpm_ir_eigv_kshell_s2_pgp.txt",
"results/ekpm/ekpm_ir_eigv_prb_s1/ekpm_ir_eigv_prb_s1_pgp.txt",
"results/ekpm/ekpm_ir_eigv_prb_s2/ekpm_ir_eigv_prb_s2_pgp.txt",
"results/ekpm/ekpm_ir_eigv_s1/ekpm_ir_eigv_s1_pgp.txt",
"results/ekpm/ekpm_ir_eigv_s2/ekpm_ir_eigv_s2_pgp.txt",
"results/ekpm/normal_s1/ekpm_default_s1_pgp.txt",
"results/ekpm/normal_s2/ekpm_default_s2_pgp.txt",
"results/gwim/normal/gwim_default_normal_test_pgp.txt",
]

astro
[
"results/ekpm/ekpm_ir_gwim_s1/ekpm_ir_gwim_s1.txt",
"results/ekpm/ekpm_ir_gwim_s2/ekpm_ir_gwim_s2.txt",
"results/ekpm/ekpm_ir_eigv_kshell_prb_s1/ekpm_ir_eigv_kshell_prb_s1.txt",
"results/ekpm/ekpm_ir_eigv_kshell_prb_s2/ekpm_ir_eigv_kshell_prb_s2.txt",
"results/ekpm/ekpm_ir_eigv_kshell_s1/ekpm_ir_eigv_kshell_s1.txt",
"results/ekpm/ekpm_ir_eigv_kshell_s2/ekpm_ir_eigv_kshell_s2.txt",
"results/ekpm/ekpm_ir_eigv_prb_s1/ekpm_ir_eigv_prb_s1.txt",
"results/ekpm/ekpm_ir_eigv_prb_s2/ekpm_ir_eigv_prb_s2.txt",
"results/ekpm/ekpm_ir_eigv_s1/ekpm_ir_eigv_s1.txt",
"results/ekpm/ekpm_ir_eigv_s2/ekpm_ir_eigv_s2.txt",
"results/ekpm/normal_s1/ekpm_default_s1.txt",
"results/ekpm/normal_s2/ekpm_default_s2.txt",
"results/gwim/normal/gwim_default_normal_test.txt",
]
---

"""
