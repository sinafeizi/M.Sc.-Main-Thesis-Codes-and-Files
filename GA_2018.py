from random import choice, choices, randint, randrange, random
from math import floor
from functions import cloning
from time import time


def build_chromosome(list_of_all_pairings, list_of_all_flights):
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
    a_population = [build_chromosome(list_of_all_pairings, list_of_all_flights)]
    while_counter = 0
    while len(a_population) < size and while_counter < 100*len(a_population):
        creation = build_chromosome(list_of_all_pairings, list_of_all_flights)
        if creation not in a_population:
            a_population.append(creation)
        else:
            while_counter += 1
    while len(a_population) < size:
        creation = build_chromosome(list_of_all_pairings, list_of_all_flights)
        a_population.append(creation)
    return a_population


def make_feasible_1(a_chromosome, list_of_all_pairings, list_of_all_flights):
    covered_flights = []
    for i in range(len(a_chromosome)):
        if a_chromosome[i] == 1:
            for j in range(len(list_of_all_pairings[i]) - 1):
                if list_of_all_pairings[i][j] not in covered_flights:
                    covered_flights.append(list_of_all_pairings[i][j])
    if len(covered_flights) == len(list_of_all_flights):
        return a_chromosome
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
        for ppp in range(len(a_chromosome)):
            if list_of_all_pairings[ppp] in selected_pairings and a_chromosome[ppp] == 0:
                a_chromosome[ppp] = 1
                added_counter += 1
            else:
                pass
        return a_chromosome


def make_feasible_2(a_chromosome, list_of_all_pairings, list_of_all_flights):
    covered_flights = []
    for i in range(len(a_chromosome)):
        if a_chromosome[i] == 1:
            for j in range(len(list_of_all_pairings[i]) - 1):
                if list_of_all_pairings[i][j] not in covered_flights:
                    covered_flights.append(list_of_all_pairings[i][j])
    if len(covered_flights) == len(list_of_all_flights):
        return a_chromosome
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
                return pairing[0][-1]*10000
        while len(covered_flights) < len(list_of_all_flights):
            uncovered_flights = []
            for c1 in list_of_all_flights:
                if c1 not in covered_flights:
                    uncovered_flights.append(c1)
            unused_pairings = []
            for c2 in range(len(list_of_all_pairings)):
                if a_chromosome[c2] == 0:
                    unused_pairings.append([list_of_all_pairings[c2], c2])
            unused_pairings = sorted(unused_pairings, key=lambda a_pair: effective_cost(a_pair, uncovered_flights))
            for c5 in unused_pairings[0][0]:
                if c5 in uncovered_flights:
                    covered_flights.append(c5)
            a_chromosome[unused_pairings[0][1]] = 1
        return a_chromosome


def make_feasible_3(a_chromosome, list_of_all_pairings, list_of_all_flights):
    covered_flights = []
    for i in range(len(a_chromosome)):
        if a_chromosome[i] == 1:
            for j in range(len(list_of_all_pairings[i]) - 1):
                if list_of_all_pairings[i][j] not in covered_flights:
                    covered_flights.append(list_of_all_pairings[i][j])
    if len(covered_flights) == len(list_of_all_flights):
        return a_chromosome
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
                return pairing[0][-1]*10000
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
                a_chromosome[covering_pairings[0][1]] = 1
                for j in range(len(selected_pairing) - 1):
                    if selected_pairing[j] not in covered_flights:
                        covered_flights.append(selected_pairing[j])
        return a_chromosome


def remove_extra_pairings(a_chromosome, list_of_all_pairings):
    main_counter = 0
    for i in range(len(a_chromosome)):
        if a_chromosome[i] == 1:
            counter1 = 0
            for j in range(len(list_of_all_pairings[i]) - 1):
                counter2 = 0
                for k in range(len(a_chromosome)):
                    if a_chromosome[k] == 1 and k != i:
                        if list_of_all_pairings[i][j] in list_of_all_pairings[k]:
                            counter2 += 1
                if counter2 >= 1:
                    counter1 += 1
            if counter1 == len(list_of_all_pairings[i]) - 1:
                a_chromosome[i] = 0
                main_counter += 1
            else:
                pass
    return a_chromosome


def is_feasible(a_chromosome, list_of_all_pairings, list_of_all_flights):
    covered_flights_1 = []
    for i001 in range(len(a_chromosome)):
        if a_chromosome[i001] == 1:
            for i002 in range(len(list_of_all_pairings[i001]) - 1):
                if list_of_all_pairings[i001][i002] not in covered_flights_1:
                    covered_flights_1.append(list_of_all_pairings[i001][i002])
    if len(covered_flights_1) == len(list_of_all_flights):
        return True
    else:
        return False


def hill_climb(a_chromosome, list_of_all_pairings, list_of_all_flights):
    list_of_better_chromosomes = []
    first_cost = cost_func(a_chromosome, list_of_all_pairings)
    for i001 in range(len(a_chromosome)):
        if a_chromosome[i001] == 1:
            covered_flights_2 = []
            un_co_flights = []
            for i002 in range(len(a_chromosome)):
                if a_chromosome[i002] == 1 and i002 != i001:
                    for i003 in range(len(list_of_all_pairings[i002]) - 1):
                        if list_of_all_pairings[i002][i003] not in covered_flights_2:
                            covered_flights_2.append(list_of_all_pairings[i002][i003])
            for i004 in list_of_all_flights:
                if i004 not in covered_flights_2:
                    un_co_flights.append(i004)
            if len(un_co_flights) == 0:
                a_chromosome[i001] = 0
                first_cost -= list_of_all_pairings[i001][-1]
            else:
                for i005 in range(len(a_chromosome)):
                    if a_chromosome[i005] == 0:
                        new_c = 0
                        for i006 in un_co_flights:
                            if i006 in list_of_all_pairings[i005]:
                                new_c += 1
                        if new_c == len(un_co_flights):
                            new_cost = 0
                            new = []
                            new.extend(a_chromosome)
                            new[i001] = 0
                            new[i005] = 1
                            for ijk in range(len(new)):
                                if new[ijk] == 1:
                                    new_cost += list_of_all_pairings[ijk][-1]
                            if int(new_cost) < int(first_cost):
                                list_of_better_chromosomes.append(cloning(new))
    if len(list_of_better_chromosomes) > 0:
        list_of_better_chromosomes = sorted(
        list_of_better_chromosomes,
        key=lambda chromosome: cost_func(chromosome, list_of_all_pairings)
    )
        return list_of_better_chromosomes[0]
    else:
        return a_chromosome


def fitness_func(a_chromosome, list_of_all_pairings):
    cost = 0
    saving = 0
    for i in a_chromosome:
        if i == 1:
            cost += list_of_all_pairings[i][-1]
        else:
            saving += list_of_all_pairings[i][-1]
    return saving/(cost*100)


def cost_func(a_chromosome, list_of_all_pairings):
    cost = 0
    for i in a_chromosome:
        if i == 1:
            cost += list_of_all_pairings[i][-1]
    return cost


def select_parents(a_population):
    if len(a_population) < 2:
        raise ValueError("population too small to select a pair of parents.")
    if len(a_population) == 2:
        parents = a_population
        return parents
    else:
        parents = choices(a_population,
                          weights=[(len(a_population) - a_population.index(i))/len(a_population) for i in a_population], k=2)
        while parents[0] == parents[1]:
            parents = choices(a_population,
                              weights=[(len(a_population) - a_population.index(i))/len(a_population) for i in a_population], k=2)
    return parents


def one_point_crossover_func(parents):
    if len(parents[0]) != len(parents[1]):
        raise ValueError("chromosomes a and b must be of same length")
    if len(parents) != 2:
        raise ValueError("more or less than two parents were given to the crossover function.")
    length = len(parents[0])
    if length < 2:
        return parents
    if 1 in parents[0] and 1 in parents[1]:
        start_point = min(parents[0].index(1), parents[1].index(1))
        end_point = max((len(parents[0]) - 1 - parents[0][::-1].index(1)),
                        (len(parents[1]) - 1 - parents[1][::-1].index(1)))
        p = randint(min(start_point + 1, end_point), end_point)
        return [parents[0][0:p] + parents[1][p:], parents[1][0:p] + parents[0][p:]]
    if 1 not in parents[0] and 1 in parents[1]:
        start_point = parents[1].index(1)
        end_point = (len(parents[1]) - 1 - parents[1][::-1].index(1))
        p = randint(min(start_point + 1, end_point), end_point)
        return [parents[0][0:p] + parents[1][p:], parents[1][0:p] + parents[0][p:]]
    if 1 in parents[0] and 1 not in parents[1]:
        start_point = parents[0].index(1)
        end_point = (len(parents[0]) - 1 - parents[0][::-1].index(1))
        p = randint(min(start_point + 1, end_point), end_point)
        return [parents[0][0:p] + parents[1][p:], parents[1][0:p] + parents[0][p:]]
    else:
        return parents


def two_point_crossover_func(parents):
    if len(parents[0]) != len(parents[1]):
        raise ValueError("chromosomes a and b must be of same length")
    if len(parents) != 2:
        raise ValueError("more or less than two parents were given to the crossover function.")
    length = len(parents[0])
    if length < 2:
        return parents
    if length == 2:
        p = 1
        return [parents[0][0:p] + parents[1][p:], parents[1][0:p] + parents[0][p:]]
    if length == 3:
        p1 = 1
        p2 = 2
        return [parents[0][0:p1] + parents[1][p1:p2] + parents[0][p2:],
                parents[1][0:p1] + parents[0][p1:p2] + parents[1][p2:]]
    else:  # it means if length >= 4
        if 1 in parents[0] and 1 in parents[1]:
            start_point = min(parents[0].index(1), parents[1].index(1))
            end_point = max((len(parents[0]) - 1 - parents[0][::-1].index(1)),
                            (len(parents[1]) - 1 - parents[1][::-1].index(1)))
            selection_length = floor((end_point - start_point + 1)/2)
            p1 = randint(min(end_point, start_point + 1), start_point + selection_length)
            p2 = randint(start_point + selection_length + 1, max(end_point, start_point + selection_length + 1))
            return [parents[0][0:p1] + parents[1][p1:p2] + parents[0][p2:],
                    parents[1][0:p1] + parents[0][p1:p2] + parents[1][p2:]]
        if 1 not in parents[0] and 1 in parents[1]:
            start_point = parents[1].index(1)
            end_point = (len(parents[1]) - 1 - parents[1][::-1].index(1))
            selection_length = floor((end_point - start_point + 1) / 2)
            p1 = randint(min(end_point, start_point + 1), start_point + selection_length)
            p2 = randint(start_point + selection_length + 1, max(end_point, start_point + selection_length + 1))
            return [parents[0][0:p1] + parents[1][p1:p2] + parents[0][p2:],
                    parents[1][0:p1] + parents[0][p1:p2] + parents[1][p2:]]
        if 1 in parents[0] and 1 not in parents[1]:
            start_point = parents[0].index(1)
            end_point = (len(parents[0]) - 1 - parents[0][::-1].index(1))
            selection_length = floor((end_point - start_point + 1) / 2)
            p1 = randint(min(end_point, start_point + 1), start_point + selection_length)
            p2 = randint(start_point + selection_length + 1, max(end_point, start_point + selection_length + 1))
            return [parents[0][0:p1] + parents[1][p1:p2] + parents[0][p2:],
                    parents[1][0:p1] + parents[0][p1:p2] + parents[1][p2:]]
        else:
            return parents


def mutation(a_chromosome, probability: float):
    if len(a_chromosome) <= 20:
        index = randrange(len(a_chromosome))
        a_chromosome[index] = a_chromosome[index] if random() > probability else abs(a_chromosome[index] - 1)
        return a_chromosome
    else:
        number_of_changes = randrange(4, 10)
        indexes = [choice(range(len(a_chromosome)))]
        while len(indexes) < number_of_changes:
            new_index = choice(range(len(a_chromosome)))
            if new_index not in indexes:
                indexes.append(new_index)
        for j50 in indexes:
            a_chromosome[j50] = a_chromosome[j50] if random() > probability else abs(a_chromosome[j50] - 1)
        return a_chromosome


def run_evolution_2018(
        list_of_all_pairings,
        list_of_all_flights,
        mutation_probability: float,
        initial_population_size: int,
        generation_limit: int,
        start_time,
        time_limit: int,
        c1: int,
        c2: int
):
    population = build_population(list_of_all_pairings, list_of_all_flights, initial_population_size)
    generation_counter = 0
    for i21 in population:
        remove_extra_pairings(i21, list_of_all_pairings)
    population = sorted(
        population,
        key=lambda chromosome: cost_func(chromosome, list_of_all_pairings)
    )
    new_file11 = open("results_GA_2018.txt", "a")
    new_file11.write("A NEW RUN!! example number: " + str(c1 + 1) + " ,try number: " + str(c2 + 1))
    new_file11.write("\n")
    new_file11.write(str(round(time() - start_time, 3)))
    new_file11.write(" ")
    new_file11.write(str(cost_func(population[0], list_of_all_pairings)))
    new_file11.write("\n")
    new_file11.close()
    for i in range(generation_limit):
        generation_counter += 1
        print("generation", generation_counter, "of", generation_limit,
              ", cost is:", cost_func(population[0], list_of_all_pairings))
        if (round(time() - start_time, 3)) > time_limit:
            break
        best_cost = cost_func(population[0], list_of_all_pairings)
        for j in range(int(len(population)/2)):
            parents = select_parents(population)
            if random() >= 0.2:
                offsprings = two_point_crossover_func(parents)
            else:
                offsprings = one_point_crossover_func(parents)
            offsprings[0] = mutation(offsprings[0], mutation_probability)
            offsprings[1] = mutation(offsprings[1], mutation_probability)
            make_feasible_1(offsprings[0], list_of_all_pairings, list_of_all_flights)
            remove_extra_pairings(offsprings[0], list_of_all_pairings)
            #hill_climb(offsprings[0], list_of_all_pairings, list_of_all_flights)
            make_feasible_1(offsprings[1], list_of_all_pairings, list_of_all_flights)
            remove_extra_pairings(offsprings[1], list_of_all_pairings)
            #hill_climb(offsprings[1], list_of_all_pairings, list_of_all_flights)
            next_generation = [offsprings[0], offsprings[1], parents[0], parents[1]]
            sorted(
                next_generation,
                key=lambda chromosome: cost_func(chromosome, list_of_all_pairings)
            )
            population.pop()
            population.pop()
            population.append(next_generation[0])
            population.append(next_generation[1])
            population = sorted(
                population,
                key=lambda chromosome: cost_func(chromosome, list_of_all_pairings)
            )
        if cost_func(population[0], list_of_all_pairings) < best_cost:
            new_file11 = open("results_GA_2018.txt", "a")
            new_file11.write(str(round(time() - start_time, 3)))
            new_file11.write(" ")
            new_file11.write(str(cost_func(population[0], list_of_all_pairings)))
            new_file11.write("\n")
            new_file11.close()
            hill_climb(population[0], list_of_all_pairings, list_of_all_flights)
    population = sorted(
        population,
        key=lambda chromosome: cost_func(chromosome, list_of_all_pairings)
    )
    print("number of generations: ", generation_counter)
    return population[0]

