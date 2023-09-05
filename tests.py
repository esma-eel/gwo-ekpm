import json
import ast
import datetime


def sum_times(times):
    total = datetime.timedelta()
    for time in times:
        (hour, minute, seconds) = time.split(":")
        delta = datetime.timedelta(
            hours=int(hour), minutes=int(minute), seconds=float(seconds)
        )
        total += delta

    return total


def find_actions(list, action_name):
    results = []
    for data in list:
        if type(data) == str:
            continue

        if data.get("action") == action_name:
            results.append(data)

    return results


def find_calculate_fitness(list):
    results = find_actions(list, "calculate_fitness")
    iterations = []
    for index, item in enumerate(results):
        if item.get("iteration"):
            new_data = {**item, **results[index + 1]}
            iterations.append(new_data)

    return iterations


with open("outputlog_ek_ir_gwim_s1_pgp-copy.txt", "r") as opened_file:
    data = opened_file.readlines()


cleaned_data = []
for line in data:
    changed_line = line.replace("'", '"')
    changed_line = line.replace("\n", "")

    if line.startswith("{"):
        changed_line = ast.literal_eval(changed_line)

    cleaned_data.append(changed_line)

# find min and max calculate fitness
calc_f = find_calculate_fitness(cleaned_data)
times = []
for item in calc_f:
    times.append(item.get("time"))

print("min time fitness")
print(min(times))

print("max time fitness")
print(max(times))


alpha_histories = find_actions(cleaned_data, "register_alpha_history")
# print(alpha_histories)

alpha_values = []
for item in alpha_histories:
    value = item.get("value")

    alpha_values.append(value)


print("min alpha")
print(min(alpha_values))

print("max alpha")
print(max(alpha_values))


ic_sim_results = find_actions(cleaned_data, "ic_simulation_result")
# print(alpha_histories)

ic_values = []
for item in ic_sim_results:
    value = item.get("spread")
    ic_values.append(value)

print("sum all activated nodes")
print(ic_values[-1])


print("influence")
finished_algorithm = find_actions(cleaned_data, "display_finished_algorithm")[0]
# print(finished_algorithm)
algorithm_result = finished_algorithm["algorithm_result"]
network_size = algorithm_result["network_size"]
ic = algorithm_result["ic"]

influence = ic / network_size
print(round(influence, 3))

print("execution time")
print(finished_algorithm["time"])


# calculate_fitness = find_actions(cleaned_data, "calculate_fitness")
# for item in calculate_fitness:
#     print(item)
# print(len(calculate_fitness))


# print(find_calculate_fitness(cleaned_data))


#     if times.get(item.get("iteration")):
# times[item.get("iteration")].append(item.get("time"))
#     else:
#         times[item.get("iteration")] = [item.get("time")]


# print(max(max(times.values())))
# print(min(min(times.values())))


# print(times)
# maxes = {}
# for iteration_number in times.keys():
#     it_times = max(times[iteration_number])
#     maxes[iteration_number] = str(it_times)

# print(maxes)
# max of calculatin of fitness value
# print(max(maxes.values()))


# lowes = {}
# for iteration_number in times.keys():
#     it_times = min(times[iteration_number])
#     lowes[iteration_number] = str(it_times)

# print(lowes)
# min of calculatin of fitness value
# print(min(maxes.values()))


# final = {}
# for iteration_number in times.keys():
#     it_times = sum_times(times[iteration_number])
#     final[iteration_number] = str(it_times)

# print(final)
