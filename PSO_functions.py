from random import choice, random
from math import exp
from functions import cloning
from time import time

def build_particle(list_of_all_pairings, list_of_all_flights):
    selected_pairings = []
    covered_flights = []
    for flight in list_of_all_flights:
        if flight not in covered_flights:
            covering_pairings = []
            for p in range(len(list_of_all_pairings)):
                if flight in list_of_all_pairings[p]:
                    covering_pairings.append(list_of_all_pairings[p])
            selected_pairing = choice(covering_pairings)
            for j in range(len(selected_pairing) - 1):
                if selected_pairing[j] not in covered_flights:
                    covered_flights.append(selected_pairing[j])
            selected_pairings.append(selected_pairing)
        else:
            pass
    one_counter = 0
    indexes = []
    for ppp in range(len(list_of_all_pairings)):
        if list_of_all_pairings[ppp] in selected_pairings:
            indexes.append(1)
            one_counter += 1
        else:
            indexes.append(0)
    return indexes


def build_population(list_of_all_pairings, list_of_all_flights, size: int):
    a_population = [build_particle(list_of_all_pairings, list_of_all_flights)]
    while_counter = 0
    while len(a_population) < size and while_counter < 100 * len(a_population):
        creation = build_particle(list_of_all_pairings, list_of_all_flights)
        if creation not in a_population:
            a_population.append(creation)
        else:
            while_counter += 1
    while len(a_population) < size:
        creation = build_particle(list_of_all_pairings, list_of_all_flights)
        a_population.append(creation)
    return a_population


def make_feasible_1(a_particle, list_of_all_pairings, list_of_all_flights):
    covered_flights = []
    for i in range(len(a_particle)):
        if a_particle[i] == 1:
            for j in range(len(list_of_all_pairings[i]) - 1):
                if list_of_all_pairings[i][j] not in covered_flights:
                    covered_flights.append(list_of_all_pairings[i][j])
    if len(covered_flights) == len(list_of_all_flights):
        return a_particle
    else:
        selected_pairings = []
        for flight in list_of_all_flights:
            if flight not in covered_flights:
                covering_pairings = []
                for p in range(len(list_of_all_pairings)):
                    if flight in list_of_all_pairings[p]:
                        covering_pairings.append(list_of_all_pairings[p])
                selected_pairing = choice(covering_pairings)
                for j in range(len(selected_pairing) - 1):
                    if selected_pairing[j] not in covered_flights:
                        covered_flights.append(selected_pairing[j])
                selected_pairings.append(selected_pairing)
            else:
                pass
        added_counter = 0
        for ppp in range(len(a_particle)):
            if list_of_all_pairings[ppp] in selected_pairings and a_particle[ppp] == 0:
                a_particle[ppp] = 1
                added_counter += 1
            else:
                pass
        return a_particle


def make_feasible_2(a_particle, list_of_all_pairings, list_of_all_flights):
    covered_flights = []
    for i in range(len(a_particle)):
        if a_particle[i] == 1:
            for j in range(len(list_of_all_pairings[i]) - 1):
                if list_of_all_pairings[i][j] not in covered_flights:
                    covered_flights.append(list_of_all_pairings[i][j])
    if len(covered_flights) == len(list_of_all_flights):
        return a_particle
    else:
        def effective_cost(pairing, flights):
            counter = 0
            for i2 in flights:
                if i2 in pairing[0]:
                    counter += 1
            if counter > 0:
                cost = pairing[0][-1] / counter
                return cost
            else:
                return pairing[0][-1] * 10000

        while len(covered_flights) < len(list_of_all_flights):
            uncovered_flights = []
            for c1 in list_of_all_flights:
                if c1 not in covered_flights:
                    uncovered_flights.append(c1)
            unused_pairings = []
            for c2 in range(len(list_of_all_pairings)):
                if a_particle[c2] == 0:
                    unused_pairings.append([list_of_all_pairings[c2], c2])
            unused_pairings = sorted(unused_pairings, key=lambda a_pair: effective_cost(a_pair, uncovered_flights))
            for c5 in unused_pairings[0][0]:
                if c5 in uncovered_flights:
                    covered_flights.append(c5)
            a_particle[unused_pairings[0][1]] = 1
        return a_particle


def make_feasible_3(a_particle, list_of_all_pairings, list_of_all_flights):
    covered_flights = []
    for i in range(len(a_particle)):
        if a_particle[i] == 1:
            for j in range(len(list_of_all_pairings[i]) - 1):
                if list_of_all_pairings[i][j] not in covered_flights:
                    covered_flights.append(list_of_all_pairings[i][j])
    if len(covered_flights) == len(list_of_all_flights):
        return a_particle
    else:
        def effective_cost(pairing, flights):
            counter = 0
            for i2 in flights:
                if i2 in pairing[0]:
                    counter += 1
            if counter > 0:
                cost = pairing[0][-1] / counter
                return cost
            else:
                return pairing[0][-1] * 10000

        while len(covered_flights) < len(list_of_all_flights):
            uncovered_flights = []
            for c1 in list_of_all_flights:
                if c1 not in covered_flights:
                    uncovered_flights.append(c1)
            for flight in uncovered_flights:
                covering_pairings = []
                for p in range(len(list_of_all_pairings)):
                    if flight in list_of_all_pairings[p]:
                        covering_pairings.append([list_of_all_pairings[p], p])
                covering_pairings = sorted(covering_pairings,
                                           key=lambda a_pair: effective_cost(a_pair, uncovered_flights))
                selected_pairing = cloning(covering_pairings[0][0])
                a_particle[covering_pairings[0][1]] = 1
                for j in range(len(selected_pairing) - 1):
                    if selected_pairing[j] not in covered_flights:
                        covered_flights.append(selected_pairing[j])
        return a_particle


def remove_extra_pairings(a_particle, list_of_all_pairings):
    main_counter = 0
    for i in range(len(a_particle)):
        if a_particle[i] == 1:
            counter1 = 0
            for j in range(len(list_of_all_pairings[i]) - 1):
                counter2 = 0
                for k in range(len(a_particle)):
                    if a_particle[k] == 1 and k != i:
                        if list_of_all_pairings[i][j] in list_of_all_pairings[k]:
                            counter2 += 1
                if counter2 >= 1:
                    counter1 += 1
            if counter1 == len(list_of_all_pairings[i]) - 1:
                a_particle[i] = 0
                main_counter += 1
            else:
                pass
    return a_particle


def fitness_func(a_particle, list_of_all_pairings):
    cost = 0
    saving = 0
    for i in a_particle:
        if i == 1:
            cost += list_of_all_pairings[i][-1]
        else:
            saving += list_of_all_pairings[i][-1]
    return saving / (cost * 100)


def cost_func(a_particle, list_of_all_pairings):
    cost = 0
    for i in a_particle:
        if i == 1:
            cost += list_of_all_pairings[i][-1]
    return cost


def sigmoid_function(a_number):
    result = exp(a_number) / (exp(a_number) + 1)
    return float(result)


def run_pso(
        list_of_all_pairings,
        list_of_all_flights,
        fee,
        fee1,
        fee2,
        v_max,
        population_size: int,
        iteration_limit: int,
        start_time,
        time_limit: int,
        c1: int,
        c2: int
):
    population = build_population(list_of_all_pairings, list_of_all_flights, population_size)
    iteration_counter = 0
    for i50 in population:
        remove_extra_pairings(i50, list_of_all_pairings)
    velocities = []
    for i51 in range(len(population)):
        velocities.append([])
    for i52 in range(len(population)):
        for i53 in range(len(population[i52])):
            if population[i52][i53] == 1:
                velocities[i52].append(7.5)
            else:
                velocities[i52].append(-6.0)
    best_positions = []
    for i47 in range(len(population)):
        best_positions.append([])
    for i48 in range(len(population)):
        for i49 in range(len(population[i48])):
            if population[i48][i49] == 1:
                best_positions[i48].append(1)
            else:
                best_positions[i48].append(0)
    best_cost_array = []
    current_cost_array = []
    for i54 in best_positions:
        best_cost_array.append(cost_func(i54, list_of_all_pairings))
    new_file12 = open("results_PSO.txt", "a")
    new_file12.write("A NEW RUN!! example number: " + str(c1 + 1) + " ,try number: " + str(c2 + 1))
    new_file12.write("\n")
    new_file12.write(str(round(time() - start_time, 3)))
    new_file12.write(" ")
    new_file12.write(str(min(best_cost_array)))
    new_file12.write("\n")
    new_file12.close()
    if (round(time() - start_time, 3)) > time_limit:
        print("Iteration ", iteration_counter, " out of ", iteration_limit, ",", "particle number ",
              best_cost_array.index(min(best_cost_array)), " reached the goal, cost: ", min(best_cost_array),
              " , END OF THE OPTIMIZATION ALGORITHM!")
        return True
    for i544 in population:
        current_cost_array.append(cost_func(i544, list_of_all_pairings))
    global_best = cloning(best_positions[best_cost_array.index(min(best_cost_array))])
    for i55 in range(len(velocities)):
        for i56 in range(len(velocities[i55])):
            velocities[i55][i56] = int(velocities[i55][i56])
            best_positions[i55][i56] = int(best_positions[i55][i56])
            population[i55][i56] = int(population[i55][i56])
    print("Iteration ", iteration_counter, " out of ", iteration_limit, ",", "particle number ",
          best_cost_array.index(min(best_cost_array)), " is the best, cost: ", min(best_cost_array))
    for i66 in range(iteration_limit):
        iteration_counter += 1
        for i67 in range(len(velocities)):
            for i68 in range(len(velocities[i67])):
                if velocities[i67][i68] <= 0:
                    velocities[i67][i68] = ((1 * velocities[i67][i68]) +
                                            (fee1 * (best_positions[i67][i68] - population[i67][i68])) +
                                            (fee2 * (global_best[i68] - population[i67][i68])))
                else:
                    velocities[i67][i68] = ((fee * velocities[i67][i68]) +
                                            (fee1 * (best_positions[i67][i68] - population[i67][i68])) +
                                            (fee2 * (global_best[i68] - population[i67][i68])))
        for k20 in range(len(velocities)):
            for k21 in range(len(velocities[k20])):
                if abs(velocities[k20][k21]) > v_max and velocities[k20][k21] > 0:
                    velocities[k20][k21] = v_max
                if abs(velocities[k20][k21]) > v_max and velocities[k20][k21] < 0:
                    velocities[k20][k21] = -v_max + 0.5
                else:
                    pass
        for i69 in range(len(population)):
            for i70 in range(len(population[i69])):
                if random() < sigmoid_function(velocities[i69][i70]):
                    population[i69][i70] = 1
                else:
                    population[i69][i70] = 0
        for i71 in population:
            make_feasible_1(i71, list_of_all_pairings, list_of_all_flights)
        for i72 in population:
            remove_extra_pairings(i72, list_of_all_pairings)
        for i733 in range(len(population)):
            current_cost_array[i733] = cost_func(population[i733], list_of_all_pairings)
        for i73 in range(len(population)):
            if cost_func(population[i73], list_of_all_pairings) < cost_func(best_positions[i73], list_of_all_pairings):
                best_positions[i73] = cloning(population[i73])
                best_cost_array[i73] = cost_func(best_positions[i73], list_of_all_pairings)
        print("current: ", current_cost_array)
        print("best: ", best_cost_array)
        if min(best_cost_array) < cost_func(global_best, list_of_all_pairings):
            print("NEW BEST SOLUTION, NEW BEST SOLUTION, NEW BEST SOLUTION, NEW BEST SOLUTION, NEW BEST SOLUTION")
            global_best = cloning(best_positions[best_cost_array.index(min(best_cost_array))])
            new_file12 = open("results_PSO.txt", "a")
            new_file12.write(str(round(time() - start_time, 3)))
            new_file12.write(" ")
            new_file12.write(str(min(best_cost_array)))
            new_file12.write("\n")
            new_file12.close()
        print("Iteration ", iteration_counter, " out of ", iteration_limit, ",", "particle number ",
              best_cost_array.index(min(best_cost_array)), " is the best, cost: ", min(best_cost_array))
        print("best particle: ", cost_func(global_best, list_of_all_pairings))
        if (round(time() - start_time, 3)) > time_limit:
            print("Iteration ", iteration_counter, " out of ", iteration_limit, ",", "particle number ",
                  best_cost_array.index(min(best_cost_array)), " reached the goal, cost: ", min(best_cost_array),
                  " , END OF THE OPTIMIZATION ALGORITHM!")
            return True
