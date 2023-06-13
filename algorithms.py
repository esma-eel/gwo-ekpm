import copy

from independent_cascade import independent_cascade_simulation
from utils import calculate_average_movement
from wolf import Wolf


def gwolf(**gwolf_args):
    """
    main function of gwim algorithm and running independent cascade for
    alpha wolf seed set
    """
    population_size = gwolf_args.get("population_size")
    graph = gwolf_args.get("graph")
    seed_set_size = gwolf_args.get("seed_set_size_start")
    fitness_function = gwolf_args.get("cost_function")
    max_t = gwolf_args.get("max_t")
    wolf_average_movement = gwolf_args.get("average_movement")

    alpha_history = []
    # iteration counter
    iteration = 0  # iteration 0 is starter iteration
    print({"iteration": iteration, "action": "generate_population"})
    population = [
        Wolf(average_movement=wolf_average_movement)
        for _ in range(population_size)
    ]

    for wolf in population:
        print(
            {
                "iteration": iteration,
                "action": "generate_position",
                "wolf": wolf.id,
            }
        )

        wolf.random_position(graph=graph)
        print(
            {
                "iteration": iteration,
                "action": "generate_seed_set",
                "wolf": wolf.id,
            }
        )
        wolf.generate_corresponding_seed_set(
            graph=graph, seed_set_size=seed_set_size
        )
        print(
            {
                "iteration": iteration,
                "action": "display_seed_set",
                "wolf": wolf.id,
                "seed_set": hash(tuple(wolf.S)),
            }
        )
        print(
            {
                "iteration": iteration,
                "action": "calculate_fitness",
                "wolf": wolf.id,
            }
        )
        fitness_value = fitness_function(
            seed_set=wolf.S,
            position=wolf.X,
            **gwolf_args,
        )
        wolf.value = fitness_value
        print({"iteration": iteration, "wolf": wolf.id, "value": wolf.value})

    print(
        {
            "iteration": iteration,
            "action": "extract_top_wolves",
        }
    )
    population = sorted(
        population,
        key=lambda wolf: wolf.value,
        reverse=True,
    )
    alpha, beta, delta = copy.copy(population[:3])
    print(
        {
            "iteration": iteration,
            "action": "display_top_wolves",
            "alpha": {
                "wolf": alpha.id,
                "value": alpha.value,
                "seed_set": hash(tuple(alpha.S)),
                "position": hash(tuple(alpha.X)),
            },
            "beta": {
                "wolf": beta.id,
                "value": beta.value,
                "seed_set": hash(tuple(beta.S)),
                "position": hash(tuple(beta.X.values())),
            },
            "delta": {
                "wolf": delta.id,
                "value": delta.value,
                "seed_set": hash(tuple(delta.S)),
                "position": hash(tuple(delta.X.values())),
            },
        }
    )

    # keep history of alphas before main iterations
    if alpha not in alpha_history:
        alpha_history.append(
            {
                "iteration": iteration,
                "action": "register_alpha_history",
                "wolf": alpha.id,
                "value": alpha.value,
                "seed_set": hash(tuple(alpha.S)),
                "position": hash(tuple(alpha.X.values())),
            }
        )

    # omega_wolves = population_sorted[3:]

    for iteration in range(1, max_t + 1, 1):
        print(f"---------- iteration {iteration} -----------")
        for wolf in population:
            print(
                {
                    "iteration": iteration,
                    "action": "update_position",
                    "wolf": wolf.id,
                }
            )
            wolf.update_position(
                alpha=alpha,
                beta=beta,
                delta=delta,
                iteration=iteration,
                graph=graph,
                max_t=max_t,
            )
            print(
                {
                    "iteration": iteration,
                    "action": "update_seed_set",
                    "wolf": wolf.id,
                }
            )
            wolf.generate_corresponding_seed_set(
                graph=graph,
                seed_set_size=seed_set_size,
            )
            print(
                {
                    "iteration": iteration,
                    "action": "display_seed_set",
                    "wolf": wolf.id,
                    "seed_set": hash(tuple(wolf.S)),
                }
            )

        for wolf in population:
            print(
                {
                    "iteration": iteration,
                    "action": "calculate_fitness",
                    "wolf": wolf.id,
                }
            )
            fitness_value = fitness_function(
                **gwolf_args,
                seed_set=wolf.S,
                position=wolf.X,
            )
            wolf.value = fitness_value
            print(
                {
                    "iteration": iteration,
                    "action": "display_value",
                    "wolf": wolf.id,
                    "value": wolf.value,
                }
            )

        print(
            {
                "iteration": iteration,
                "action": "extract_top_wolves",
            }
        )
        population = sorted(
            population,
            key=lambda wolf: wolf.value,
            reverse=True,
        )
        alpha, beta, delta = copy.copy(population[:3])
        print(
            {
                "iteration": iteration,
                "action": "display_top_wolves",
                "alpha": {
                    "wolf": alpha.id,
                    "value": alpha.value,
                    "seed_set": hash(tuple(alpha.S)),
                    "position": hash(tuple(alpha.X)),
                },
                "beta": {
                    "wolf": beta.id,
                    "value": beta.value,
                    "seed_set": hash(tuple(beta.S)),
                    "position": hash(tuple(beta.X.values())),
                },
                "delta": {
                    "wolf": delta.id,
                    "value": delta.value,
                    "seed_set": hash(tuple(delta.S)),
                    "position": hash(tuple(delta.X.values())),
                },
            }
        )

        # keep history of alphas during iterations
        if alpha not in alpha_history:
            alpha_history.append(
                {
                    "iteration": iteration,
                    "action": "register_alpha_history",
                    "wolf": alpha.id,
                    "value": alpha.value,
                    "seed_set": hash(tuple(alpha.S)),
                    "position": hash(tuple(alpha.X.values())),
                }
            )

        # omega_wolves = population_sorted[3:]
        if (beta.X.values() == alpha.X.values()) or (
            delta.X.values() == beta.X.values()
        ):
            print(
                {
                    "iteration": iteration,
                    "action": "regenerate_beta_position",
                    "wolf": beta.id,
                }
            )
            beta.random_position(graph=graph)

            print(
                {
                    "iteration": iteration,
                    "action": "regenerate_delta_position",
                    "wolf": delta.id,
                }
            )
            delta.random_position(graph=graph)

        if gwolf_args.get("average_movement"):
            average_movement = calculate_average_movement(
                wolves=population,
                prev_t=iteration - 1,
                current_t=iteration,
                average_movement=gwolf_args.get("average_movement"),
            )
            print(
                {
                    "iteration": iteration,
                    "action": "display_average_movement",
                    "for": str((iteration - 1, iteration)),
                    "value": average_movement,
                }
            )
    # end iteration

    print({"action": "display_population", "status": "final"})
    for wolf in population:
        print(
            {
                "wolf": wolf.id,
                "value": wolf.value,
                "seed_set": hash(tuple(wolf.S)),
                "position": hash(tuple(wolf.X.values())),
            }
        )

    print({"action": "display_alpha", "status": "final"})
    print(
        alpha,
        alpha.value,
        alpha.S,
    )

    print({"action": "display_alpha_history"})
    for u_alpha in alpha_history:
        print(u_alpha)

    print({"action": "run_ic_simulation"})
    independent_cascade_result = independent_cascade_simulation(
        seed_set=alpha.S,
        graph=graph,
        propogation_probability=gwolf_args.get("propogation_probability_start"),
        monte_carlo_simulation_number=gwolf_args.get("monte_carlo"),
    )

    print({"action": "display_ic_result"})
    print(independent_cascade_result)

    return {
        "ic": independent_cascade_result,
        "network_size": len(graph.nodes()),
        "alpha": {
            "wolf": alpha.id,
            "position": hash(tuple(alpha.X.values())),
            "seed_set": alpha.S,
        },
    }
