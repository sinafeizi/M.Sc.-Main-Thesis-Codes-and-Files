from random import choice, random
from functions import cloning
from time import time
from main import slp, to_cover_flights_list

def cost_func(a_path, list_of_all_pairings):
    cost = 0
    for i in range(len(a_path)):
        if a_path[i] == 1:
            cost += list_of_all_pairings[i][-1]
    return cost


def build_path(list_of_all_pairings, list_of_all_flights):
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


# function above builds randomly


def build_network(list_of_all_pairings, list_of_all_flights, size: int):
    a_network = [build_path(list_of_all_pairings, list_of_all_flights)]
    while_counter = 0
    while len(a_network) < size and while_counter < 100 * len(a_network):
        creation = build_path(list_of_all_pairings, list_of_all_flights)
        if creation not in a_network:
            a_network.append(creation)
        else:
            while_counter += 1
    while len(a_network) < size:
        creation = build_path(list_of_all_pairings, list_of_all_flights)
        a_network.append(creation)
    return a_network


# function above uses a random function


def make_feasible_1(a_path, list_of_all_pairings, list_of_all_flights):
    covered_flights = []
    for i in range(len(a_path)):
        if a_path[i] == 1:
            for j in range(len(list_of_all_pairings[i]) - 1):
                if list_of_all_pairings[i][j] not in covered_flights:
                    covered_flights.append(list_of_all_pairings[i][j])
    if len(covered_flights) == len(list_of_all_flights):
        return a_path
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
        for ppp in range(len(a_path)):
            if list_of_all_pairings[ppp] in selected_pairings and a_path[ppp] == 0:
                a_path[ppp] = 1
                added_counter += 1
            else:
                pass
        return a_path


def make_feasible_2(a_path, list_of_all_pairings, list_of_all_flights):
    covered_flights = []
    for i in range(len(a_path)):
        if a_path[i] == 1:
            for j in range(len(list_of_all_pairings[i]) - 1):
                if list_of_all_pairings[i][j] not in covered_flights:
                    covered_flights.append(list_of_all_pairings[i][j])
    if len(covered_flights) == len(list_of_all_flights):
        return a_path
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
                if a_path[c2] == 0:
                    unused_pairings.append([list_of_all_pairings[c2], c2])
            unused_pairings = sorted(unused_pairings, key=lambda a_pair: effective_cost(a_pair, uncovered_flights))
            for c5 in unused_pairings[0][0]:
                if c5 in uncovered_flights:
                    covered_flights.append(c5)
            a_path[unused_pairings[0][1]] = 1
        return a_path


def make_feasible_3(a_path, list_of_all_pairings, list_of_all_flights):
    covered_flights = []
    for i in range(len(a_path)):
        if a_path[i] == 1:
            for j in range(len(list_of_all_pairings[i]) - 1):
                if list_of_all_pairings[i][j] not in covered_flights:
                    covered_flights.append(list_of_all_pairings[i][j])
    if len(covered_flights) == len(list_of_all_flights):
        return a_path
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
                a_path[covering_pairings[0][1]] = 1
                for j in range(len(selected_pairing) - 1):
                    if selected_pairing[j] not in covered_flights:
                        covered_flights.append(selected_pairing[j])
        return a_path


def remove_extra_pairings(a_path, list_of_all_pairings):
    main_counter = 0
    for i in range(len(a_path)):
        if a_path[i] == 1:
            counter1 = 0
            for j in range(len(list_of_all_pairings[i]) - 1):
                counter2 = 0
                for k in range(len(a_path)):
                    if a_path[k] == 1 and k != i:
                        if list_of_all_pairings[i][j] in list_of_all_pairings[k]:
                            counter2 += 1
                if counter2 >= 1:
                    counter1 += 1
            if counter1 == len(list_of_all_pairings[i]) - 1:
                a_path[i] = 0
                main_counter += 1
            else:
                pass
    return a_path


def run_aco(
        list_of_all_pairings,
        list_of_all_flights,
        number_of_ants: int,
        generations_limit: int,
        beta,
        fee,
        start_time,
        time_limit: int,
        c1: int,
        c2: int
):
    network = build_network(list_of_all_pairings, list_of_all_flights, number_of_ants)
    generation_counter = 0
    for w01 in network:
        remove_extra_pairings(w01, list_of_all_pairings)
    pheromones = []
    for w02 in range(len(list_of_all_pairings)):
        pheromones.append(0)
    current_cost_array = []
    for w03 in network:
        current_cost_array.append(cost_func(w03, list_of_all_pairings))
    print("Generation ", generation_counter, " out of ", generations_limit, ",", "ant number ",
          current_cost_array.index(min(current_cost_array)), " is the best, cost: ", min(current_cost_array),
          ". And also ", round(time() - start_time, 3), " seconds have passed")
    new_file15 = open("results_ACO.txt", "a")
    new_file15.write("A NEW RUN!! example number: " + str(c1 + 1) + " ,try number: " + str(c2 + 1))
    new_file15.write("\n")
    new_file15.write(str(round(time() - start_time, 3)))
    new_file15.write(" ")
    new_file15.write(str(min(current_cost_array)))
    new_file15.write("\n")
    new_file15.close()
    global_best = min(current_cost_array)
    if (round(time() - start_time, 3)) > time_limit:
        print("generation ", generation_counter, " out of ", generations_limit, ", cost: ", global_best,
              " , END OF THE OPTIMIZATION ALGORITHM!")
        return True
    for w04 in range(generations_limit):
        generation_counter += 1
        delta_pheromones = []
        for w07 in range(len(list_of_all_pairings)):
            delta_pheromones.append(0)
        for w05 in range(len(network)):
            for w06 in range(len(network[w05])):
                if network[w05][w06] == 1:
                    if cost_func(network[w05], list_of_all_pairings) == global_best:
                        delta_pheromones[w06] += (
                                20*(max(current_cost_array) / cost_func(network[w05], list_of_all_pairings)))
                    elif cost_func(network[w05], list_of_all_pairings) == min(current_cost_array):
                        delta_pheromones[w06] += (
                                5*(max(current_cost_array) / cost_func(network[w05], list_of_all_pairings)))
                    else:
                        delta_pheromones[w06] += (
                                max(current_cost_array) / cost_func(network[w05], list_of_all_pairings))
        for w08 in range(len(pheromones)):
            pheromones[w08] = (pheromones[w08] * (1 - fee)) + delta_pheromones[w08]
        probabilities = []
        for w20 in range(len(list_of_all_pairings)):
            probabilities.append(0)
        for w10 in range(len(list_of_all_pairings)):
            if pheromones[w10] != 0:
                probabilities[w10] = ((pheromones[w10] * beta) / max(pheromones))
        for w09 in range(len(network)):
            for w12 in range(len(network[w09])):
                if random() < (probabilities[w12]):
                    network[w09][w12] = 1
                elif probabilities[w12] == 0 and random() < 0.0002:
                    network[w09][w12] = 1
                else:
                    network[w09][w12] = 0
        for w14 in range(len(network)):
            no_of_1s = 0
            for w15 in range(len(network[w14])):
                if network[w14][w15] == 1:
                    no_of_1s += 1
            print("generation ", w04 + 1, "ant ", w14, "number of 1s ", no_of_1s)
        for w15 in range(len(network)):
            make_feasible_1(network[w15], list_of_all_pairings, list_of_all_flights)
            remove_extra_pairings(network[w15], list_of_all_pairings)
            current_cost_array[w15] = cost_func(network[w15], list_of_all_pairings)
        if min(current_cost_array) < global_best:
            global_best = min(current_cost_array)
            print("NEW SOLUTION     NEW SOLUTION     NEW SOLUTION     NEW SOLUTION     NEW SOLUTION     NEW SOLUTION")
            new_file15 = open("results_ACO.txt", "a")
            new_file15.write(str(round(time() - start_time, 3)))
            new_file15.write(" ")
            new_file15.write(str(min(current_cost_array)))
            new_file15.write("\n")
            new_file15.close()
        print("Generation ", generation_counter, " out of ", generations_limit, ",", "ant number ",
              current_cost_array.index(min(current_cost_array)), " is the best, cost: ", min(current_cost_array),
              ". And also ", round(time() - start_time, 3), " seconds have passed")
        print("global_best: ", global_best)
        print(current_cost_array)
        if (round(time() - start_time, 3)) > time_limit:
            print("generation ", generation_counter, " out of ", generations_limit, " , cost: ",
                  global_best,
                  " , END OF THE OPTIMIZATION ALGORITHM!")
            network = sorted(
                network,
                key=lambda a_path: cost_func(a_path, list_of_all_pairings)
            )
            print(cost_func(network[0], list_of_all_pairings))
            covers =[]
            indexes = []
            new_file11 = open("cplex3.txt", "w")
            for df in range(len(list_of_all_flights)):
                cover_counter = 0
                for df2 in range(len(list_of_all_pairings)):
                    if list_of_all_flights[df] in list_of_all_pairings[df2] and network[0][df2] == 1:
                        cover_counter += 1
                        if df2 not in indexes:
                            indexes.append(df2)
                            new_file11.write(str(df2))
                            new_file11.write("\n")
                covers.append(int(cover_counter))
            new_file11.close()
            print(covers)
            print(len(covers))
            print(indexes)
            print(len(indexes))
            return True

run_aco(slp, to_cover_flights_list, 15, 100000, 1, 0.85, time(), 3600, 2, 2)