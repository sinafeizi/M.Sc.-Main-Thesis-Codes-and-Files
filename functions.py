def is_arced(flight1, flight2):
    if flight1[2] == flight2[2]:
        if 60 <= (flight2[3] - flight1[4]) and flight1[1] == flight2[0]:
            origin_flight = flight1
            destination_flight = flight2
            return True, origin_flight, destination_flight
        if 60 <= (flight1[3] - flight2[4]) and flight2[1] == flight1[0]:
            origin_flight = flight2
            destination_flight = flight1
            return True, origin_flight, destination_flight
        else:
            return False
    else:
        return False


def is_arced_arrow(flight1, flight2):
    if flight1[2] == flight2[2]:
        if 30 <= (flight2[3] - flight1[4]) <= 70 and flight1[1] == flight2[0]:
            return True
        else:
            return False
    else:
        return False


def is_arced_arrow2(flight1, flight2):
    if flight1[2] == flight2[2]:
        if 30 <= (flight2[3] - flight1[4]) <= 90 and flight1[1] == flight2[0]:
            return True
        else:
            return False
    else:
        return False



def is_pair_able(flight1, flight2):
    if 90 >= (flight2[3] - flight1[4]) >= 30 and flight1[1] == flight2[0]:
        return True
    else:
        return False


def is_complete(flight1, flight2):
    if flight1[0] == flight2[1]:
        return True
    else:
        return False


def is_too_long(dic, flight):
    pair_length_time = 0
    pair_length_count = 0
    for i in dic:
        pair_length_time += i[5]
        pair_length_count += 1
    pair_length_time += flight[5]
    pair_length_count += 1
    if pair_length_time >= 720 or pair_length_count >= 12:
        return True
    else:
        return False


def is_too_short(dic, flight):
    pair_length_time = 0
    pair_length_count = 0
    for i in dic:
        pair_length_time += i[5]
        pair_length_count += 1
    pair_length_time += flight[5]
    pair_length_count += 1
    if pair_length_time <= 180 and pair_length_count < 3:
        return True
    else:
        return False


def cloning(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy


def ds_algorithm(ff, any_matrix, stack, slp, counter, a_dic):
    counter += 1
    a_dic[counter] = cloning(stack)
    for i in ff[6]:
        if not is_too_long(a_dic[counter], any_matrix[i]):
            if is_pair_able(ff, any_matrix[i]):
                if is_complete(a_dic[counter][0], any_matrix[i]):
                    if not is_too_short(a_dic[counter], any_matrix[i]):
                        slp.append(cloning(stack) + [any_matrix[i]])
                    ds_algorithm(any_matrix[i], any_matrix, a_dic[counter] + [any_matrix[i]], slp, counter, a_dic)
                else:
                    ds_algorithm(any_matrix[i], any_matrix, a_dic[counter] + [any_matrix[i]], slp, counter, a_dic)
            else:
                pass
        else:
            pass
    return slp


def get_dp_fdp(pairing):
    dp_time = 0
    fdp_time = 0
    # getting times related to the duration of each flight
    for flight in pairing:
        if flight[5] <= 40:
            fdp_time += 40
        else:
            fdp_time += flight[5]
    # getting time related to the duration of the pairing
    if pairing[-1][4] >= pairing[0][3]:
        if (pairing[-1][4] + 30) - (pairing[0][3] - 30) <= 240:
            dp_time += 240
        else:
            dp_time += (pairing[-1][4] + 30) - (pairing[0][3] - 30)
    else:
        if ((1440 - pairing[0][3]) + pairing[-1][4]) <= 240:
            dp_time += 240
        else:
            dp_time += (1440 - pairing[0][3]) + pairing[-1][4]
    return dp_time, fdp_time


def get_cost(pairing):
    return 2*(get_dp_fdp(pairing)[1]) + 1*(get_dp_fdp(pairing)[0] - get_dp_fdp(pairing)[1])
