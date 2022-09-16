import datetime

from constants import MAX_T, POPULATION_SIZE
from cost_functions import fitness_function
from independent_cascade import independent_cascade_simulation

from utils import calculate_average_movement
from wolf import Wolf
from network import initial_graph

graph = initial_graph()


def main():
    """
    main function of gwim algorithm and running independent cascade for
    alpha wolf seed set
    """
    alpha_history = []
    # iteration counter
    print("creating population before starting main algorithm:")
    population = [Wolf() for _ in range(POPULATION_SIZE)]

    for wolf in population:
        print("generating random position for wolf: ", wolf)
        wolf.random_position(graph)
        wolf.register_position_history(0)
        print("generating random seed set for wolf: ", wolf)
        wolf.generate_corresponding_seed_set(graph)
        print("wolf ", wolf, " seed set is: ", wolf.S)
        print("generating fitness value for wolf: ", wolf)
        fitness_value = fitness_function(wolf.S, graph)
        print("fitness value of wolf ", wolf, fitness_value)
        wolf.value = fitness_value

    print("extracting alpha, beta, delta and omega wolves:")
    population_sorted = sorted(
        population,
        key=lambda wolf: wolf.value,
        reverse=True,
    )
    alpha, beta, delta = population_sorted[:3]
    omega_wolves = population_sorted[3:]

    for iteration in range(MAX_T):
        print(f"---------- iteration {iteration} -----------")
        for wolf in omega_wolves:
            print("updating position for omega wolf: ", wolf)
            wolf.update_position(alpha, beta, delta, iteration, graph)
            wolf.register_position_history(iteration)
            print("updating seed set for wolf: ", wolf)
            wolf.generate_corresponding_seed_set(graph)
            print("wolf ", wolf, " seed set is: ", wolf.S)

        for wolf in population:
            print("recalculating fitness value for wolf: ", wolf)
            fitness_value = fitness_function(wolf.S, graph)
            print("fitness value of wolf ", wolf, fitness_value)
            wolf.value = fitness_value

        print("extracting alpha, beta, delta and omega wolves:")
        population_sorted = sorted(
            population,
            key=lambda wolf: wolf.value,
            reverse=True,
        )
        alpha, beta, delta = population_sorted[:3]

        # keep history of alphas during iterations
        if alpha not in alpha_history:
            alpha_history.append(alpha)

        omega_wolves = population_sorted[3:]
        if (beta.X.values() == alpha.X.values()) or (
            delta.X.values() == beta.X.values()
        ):
            print("regenerating position for wolf beta: ", beta)
            beta.random_position(graph)
            beta.register_position_history(iteration)

            print("regenerating position for wolf delta: ", delta)
            delta.random_position(graph)
            delta.register_position_history(iteration)

        average_movement = calculate_average_movement(
            population, iteration - 1, iteration
        )
        print(
            f"average movement in: ({iteration - 1}, {iteration}) =>"
            f" {average_movement}"
        )

    for wolf in population:
        print(
            wolf,
            wolf.value,
            wolf.S,
        )

    print("Final Alpha is:")
    print(
        alpha,
        alpha.value,
        alpha.S,
    )
    print("all unique alpha throgh iterations are: ")
    for u_alpha in alpha_history:
        print(
            u_alpha,
            u_alpha.value,
            u_alpha.S,
        )
    print("running simulation of independent cascade:")
    independent_cascade_result = independent_cascade_simulation(
        seed_set=alpha.S,
        graph=graph,
    )

    print("independent cascade simulation result is:")
    print(independent_cascade_result)

    return alpha


if __name__ == "__main__":
    start_main = datetime.datetime.now()
    main()
    end_main = datetime.datetime.now()
    delta_main = end_main - start_main
    print("time of execution this algorithm: ", delta_main)
