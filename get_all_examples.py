import sys
from functions import is_arced_arrow, cloning
from functions import ds_algorithm
from functions import get_cost
sys.setrecursionlimit(1000000000)
f1 = open("small_1.txt", "r")
f2 = open("small_2.txt", "r")
f3 = open("small_3.txt", "r")
f4 = open("small_4.txt", "r")
f5 = open("medium_1.txt", "r")
f6 = open("medium_2.txt", "r")
f7 = open("medium_3.txt", "r")
f8 = open("medium_4.txt", "r")
f9 = open("large_1.txt", "r")
f10 = open("large_2.txt", "r")
f11 = open("large_3.txt", "r")
f12 = open("large_4.txt", "r")

flights_list = f1.readlines()
flights_list.extend(f2.readlines())
flights_list.extend(f3.readlines())
flights_list.extend(f4.readlines())
flights_list.extend(f5.readlines())
flights_list.extend(f6.readlines())
flights_list.extend(f7.readlines())
flights_list.extend(f8.readlines())
flights_list.extend(f9.readlines())
flights_list.extend(f10.readlines())
flights_list.extend(f11.readlines())
flights_list.extend(f12.readlines())

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()
f10.close()
f11.close()
f12.close()

number_of_flights = len(flights_list)
matrix = []
for i in range(number_of_flights):
    matrix.append(flights_list[i].split(" "))
for i in range(len(matrix)):
    matrix[i] = matrix[i][0:3] + matrix[i][3].split(":") + matrix[i][4].split(":")
for i in range(len(matrix)):
    for j in range(2, 7):
        matrix[i][j] = int(matrix[i][j])
for i in range(len(matrix)):
    matrix[i][3] = ((60*matrix[i][3]) + matrix[i][4])
    matrix[i][4] = ((60*matrix[i][5]) + matrix[i][6])
    if matrix[i][4] >= matrix[i][3]:
        matrix[i][5] = matrix[i][4] - matrix[i][3]
    else:
        matrix[i][5] = (1440 - matrix[i][3]) + matrix[i][4]
for i in matrix:
    i.pop()
for i in matrix:
    i.append([])

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if 0 <= i < 205 and 0 <= j < 205:
            if is_arced_arrow(matrix[i], matrix[j]):
                matrix[i].append(j)
        if 205 <= i < 406 and 205 <= j < 406:
            if is_arced_arrow(matrix[i], matrix[j]):
                matrix[i].append(j-205)
        if 406 <= i < 602 and 406 <= j < 602:
            if is_arced_arrow(matrix[i], matrix[j]):
                matrix[i].append(j-406)
        if 602 <= i < 805 and 602 <= j < 805:
            if is_arced_arrow(matrix[i], matrix[j]):
                matrix[i].append(j-602)
        if 805 <= i < 2644 and 805 <= j < 2644:
            if is_arced_arrow(matrix[i], matrix[j]):
                matrix[i].append(j-805)
        if 2644 <= i < 4955 and 2644 <= j < 4955:
            if is_arced_arrow(matrix[i], matrix[j]):
                matrix[i].append(j-2644)
        if 4955 <= i < 7107 and 4955 <= j < 7107:
            if is_arced_arrow(matrix[i], matrix[j]):
                matrix[i].append(j-4955)
        if 7107 <= i < 9249 and 7107 <= j < 9249:
            if is_arced_arrow(matrix[i], matrix[j]):
                matrix[i].append(j-7107)
        if 9249 <= i < 12765 and 9249 <= j < 12765:
            if is_arced_arrow(matrix[i], matrix[j]):
                matrix[i].append(j-9249)
        if 12765 <= i < 16662 and 12765 <= j < 16662:
            if is_arced_arrow(matrix[i], matrix[j]):
                matrix[i].append(j-12765)
        if 16662 <= i < 20344 and 16662 <= j < 20344:
            if is_arced_arrow(matrix[i], matrix[j]):
                matrix[i].append(j-16662)
        if 20344 <= i < 23953 and 20344 <= j < 23953:
            if is_arced_arrow(matrix[i], matrix[j]):
                matrix[i].append(j-20344)

for i in range(len(matrix)):
    matrix[i][6] = matrix[i][7:]
for i in matrix:
    tool = len(i) - 7
    for j in range(tool):
        i.pop()
matrix01 = cloning(matrix[0:205])
matrix02 = cloning(matrix[205:406])
matrix03 = cloning(matrix[406:602])
matrix04 = cloning(matrix[602:805])
matrix05 = cloning(matrix[805:2644])
matrix06 = cloning(matrix[2644:4955])
matrix07 = cloning(matrix[4955:7107])
matrix08 = cloning(matrix[7107:9249])
matrix09 = cloning(matrix[9249:12765])
matrix10 = cloning(matrix[12765:16662])
matrix11 = cloning(matrix[16662:20344])
matrix12 = cloning(matrix[20344:23953])

stacks_dic01 = {}
stacks_dic02 = {}
stacks_dic03 = {}
stacks_dic04 = {}
stacks_dic05 = {}
stacks_dic06 = {}
stacks_dic07 = {}
stacks_dic08 = {}
stacks_dic09 = {}
stacks_dic10 = {}
stacks_dic11 = {}
stacks_dic12 = {}

slp01 = []
slp02 = []
slp03 = []
slp04 = []
slp05 = []
slp06 = []
slp07 = []
slp08 = []
slp09 = []
slp10 = []
slp11 = []
slp12 = []

base_cities_small = ["13830", "12173"]
base_cities_medium = ["12478", "14869", "10397", "13204", "12892", "12953", "13487", "14747", "11433"]
base_cities_large = ["11292", "13204", "12889", "10693", "12892", "13198", "13232", "11259", "10821", "10397", "10423", "14679", "14831", "12191",
               "13796", "14107", "15016", "15304"]
for f01 in matrix01:
    if f01[0] in base_cities_small and f01[2] == 1:
        ds_algorithm(f01, matrix01, [f01], slp01, 0, stacks_dic01)
for f02 in matrix02:
    if f02[0] in base_cities_small and f02[2] == 2:
        ds_algorithm(f02, matrix02, [f02], slp02, 0, stacks_dic02)
for f03 in matrix03:
    if f03[0] in base_cities_small and f03[2] == 3:
        ds_algorithm(f03, matrix03, [f03], slp03, 0, stacks_dic03)
for f04 in matrix04:
    if f04[0] in base_cities_small and f04[2] == 4:
        ds_algorithm(f04, matrix04, [f04], slp04, 0, stacks_dic04)
for f05 in matrix05:
    if f05[0] in base_cities_medium and f05[2] == 1:
        ds_algorithm(f05, matrix05, [f05], slp05, 0, stacks_dic05)
for f06 in matrix06:
    if f06[0] in base_cities_medium and f06[2] == 2:
        ds_algorithm(f06, matrix06, [f06], slp06, 0, stacks_dic06)
for f07 in matrix07:
    if f07[0] in base_cities_medium and f07[2] == 3:
        ds_algorithm(f07, matrix07, [f07], slp07, 0, stacks_dic07)
for f08 in matrix08:
    if f08[0] in base_cities_medium and f08[2] == 4:
        ds_algorithm(f08, matrix08, [f08], slp08, 0, stacks_dic08)
for f09 in matrix09:
    if f09[0] in base_cities_large and f09[2] == 1:
        ds_algorithm(f09, matrix09, [f09], slp09, 0, stacks_dic09)
for f10 in matrix10:
    if f10[0] in base_cities_large and f10[2] == 2:
        ds_algorithm(f10, matrix10, [f10], slp10, 0, stacks_dic10)
for f11 in matrix11:
    if f11[0] in base_cities_large and f11[2] == 3:
        ds_algorithm(f11, matrix11, [f11], slp11, 0, stacks_dic11)
for f12 in matrix12:
    if f12[0] in base_cities_large and f12[2] == 4:
        ds_algorithm(f12, matrix12, [f12], slp12, 0, stacks_dic12)

for d1 in slp01:
    d1.append(get_cost(d1))
for d2 in slp02:
    d2.append(get_cost(d2))
for d3 in slp03:
    d3.append(get_cost(d3))
for d4 in slp04:
    d4.append(get_cost(d4))
for d5 in slp05:
    d5.append(get_cost(d5))
for d6 in slp06:
    d6.append(get_cost(d6))
for d7 in slp07:
    d7.append(get_cost(d7))
for d8 in slp08:
    d8.append(get_cost(d8))
for d9 in slp09:
    d9.append(get_cost(d9))
for d10 in slp10:
    d10.append(get_cost(d10))
for d11 in slp11:
    d11.append(get_cost(d11))
for d12 in slp12:
    d12.append(get_cost(d12))

to_cover_flights_list01 = []
to_cover_flights_list02 = []
to_cover_flights_list03 = []
to_cover_flights_list04 = []
to_cover_flights_list05 = []
to_cover_flights_list06 = []
to_cover_flights_list07 = []
to_cover_flights_list08 = []
to_cover_flights_list09 = []
to_cover_flights_list10 = []
to_cover_flights_list11 = []
to_cover_flights_list12 = []

for ff in matrix01:
    for pp in slp01:
        if ff in pp:
            if ff not in to_cover_flights_list01:
                to_cover_flights_list01.append(ff)
for ff in matrix02:
    for pp in slp02:
        if ff in pp:
            if ff not in to_cover_flights_list02:
                to_cover_flights_list02.append(ff)
for ff in matrix03:
    for pp in slp03:
        if ff in pp:
            if ff not in to_cover_flights_list03:
                to_cover_flights_list03.append(ff)
for ff in matrix04:
    for pp in slp04:
        if ff in pp:
            if ff not in to_cover_flights_list04:
                to_cover_flights_list04.append(ff)
for ff in matrix05:
    for pp in slp05:
        if ff in pp:
            if ff not in to_cover_flights_list05:
                to_cover_flights_list05.append(ff)
for ff in matrix06:
    for pp in slp06:
        if ff in pp:
            if ff not in to_cover_flights_list06:
                to_cover_flights_list06.append(ff)
for ff in matrix07:
    for pp in slp07:
        if ff in pp:
            if ff not in to_cover_flights_list07:
                to_cover_flights_list07.append(ff)
for ff in matrix08:
    for pp in slp08:
        if ff in pp:
            if ff not in to_cover_flights_list08:
                to_cover_flights_list08.append(ff)
for ff in matrix09:
    for pp in slp09:
        if ff in pp:
            if ff not in to_cover_flights_list09:
                to_cover_flights_list09.append(ff)
for ff in matrix10:
    for pp in slp10:
        if ff in pp:
            if ff not in to_cover_flights_list10:
                to_cover_flights_list10.append(ff)
for ff in matrix11:
    for pp in slp11:
        if ff in pp:
            if ff not in to_cover_flights_list11:
                to_cover_flights_list11.append(ff)
for ff in matrix12:
    for pp in slp12:
        if ff in pp:
            if ff not in to_cover_flights_list12:
                to_cover_flights_list12.append(ff)

for ii in range(len(slp01)):
    for jj in range(len(slp01[ii]) - 1):
        slp01[ii][jj] = slp01[ii][jj][:-1]
for ii in range(len(slp02)):
    for jj in range(len(slp02[ii]) - 1):
        slp02[ii][jj] = slp02[ii][jj][:-1]
for ii in range(len(slp03)):
    for jj in range(len(slp03[ii]) - 1):
        slp03[ii][jj] = slp03[ii][jj][:-1]
for ii in range(len(slp04)):
    for jj in range(len(slp04[ii]) - 1):
        slp04[ii][jj] = slp04[ii][jj][:-1]
for ii in range(len(slp05)):
    for jj in range(len(slp05[ii]) - 1):
        slp05[ii][jj] = slp05[ii][jj][:-1]
for ii in range(len(slp06)):
    for jj in range(len(slp06[ii]) - 1):
        slp06[ii][jj] = slp06[ii][jj][:-1]
for ii in range(len(slp07)):
    for jj in range(len(slp07[ii]) - 1):
        slp07[ii][jj] = slp07[ii][jj][:-1]
for ii in range(len(slp08)):
    for jj in range(len(slp08[ii]) - 1):
        slp08[ii][jj] = slp08[ii][jj][:-1]
for ii in range(len(slp09)):
    for jj in range(len(slp09[ii]) - 1):
        slp09[ii][jj] = slp09[ii][jj][:-1]
for ii in range(len(slp10)):
    for jj in range(len(slp10[ii]) - 1):
        slp10[ii][jj] = slp10[ii][jj][:-1]
for ii in range(len(slp11)):
    for jj in range(len(slp11[ii]) - 1):
        slp11[ii][jj] = slp11[ii][jj][:-1]
for ii in range(len(slp12)):
    for jj in range(len(slp12[ii]) - 1):
        slp12[ii][jj] = slp12[ii][jj][:-1]

for iii in range(len(to_cover_flights_list01)):
    to_cover_flights_list01[iii] = to_cover_flights_list01[iii][:-1]
for iii in range(len(to_cover_flights_list02)):
    to_cover_flights_list02[iii] = to_cover_flights_list02[iii][:-1]
for iii in range(len(to_cover_flights_list03)):
    to_cover_flights_list03[iii] = to_cover_flights_list03[iii][:-1]
for iii in range(len(to_cover_flights_list04)):
    to_cover_flights_list04[iii] = to_cover_flights_list04[iii][:-1]
for iii in range(len(to_cover_flights_list05)):
    to_cover_flights_list05[iii] = to_cover_flights_list05[iii][:-1]
for iii in range(len(to_cover_flights_list06)):
    to_cover_flights_list06[iii] = to_cover_flights_list06[iii][:-1]
for iii in range(len(to_cover_flights_list07)):
    to_cover_flights_list07[iii] = to_cover_flights_list07[iii][:-1]
for iii in range(len(to_cover_flights_list08)):
    to_cover_flights_list08[iii] = to_cover_flights_list08[iii][:-1]
for iii in range(len(to_cover_flights_list09)):
    to_cover_flights_list09[iii] = to_cover_flights_list09[iii][:-1]
for iii in range(len(to_cover_flights_list10)):
    to_cover_flights_list10[iii] = to_cover_flights_list10[iii][:-1]
for iii in range(len(to_cover_flights_list11)):
    to_cover_flights_list11[iii] = to_cover_flights_list11[iii][:-1]
for iii in range(len(to_cover_flights_list12)):
    to_cover_flights_list12[iii] = to_cover_flights_list12[iii][:-1]

print(len(to_cover_flights_list01))
print(len(slp01))
print(len(to_cover_flights_list02))
print(len(slp02))
print(len(to_cover_flights_list03))
print(len(slp03))
print(len(to_cover_flights_list04))
print(len(slp04))
print(len(to_cover_flights_list05))
print(len(slp05))
print(len(to_cover_flights_list06))
print(len(slp06))
print(len(to_cover_flights_list07))
print(len(slp07))
print(len(to_cover_flights_list08))
print(len(slp08))
print(len(to_cover_flights_list09))
print(len(slp09))
print(len(to_cover_flights_list10))
print(len(slp10))
print(len(to_cover_flights_list11))
print(len(slp11))
print(len(to_cover_flights_list12))
print(len(slp12))
list_of_slp_s = [slp01, slp02, slp03, slp04, slp05, slp06, slp07, slp08, slp09, slp10, slp11 ,slp12]
list_of_to_cover_flights_lists = [to_cover_flights_list01, to_cover_flights_list02, to_cover_flights_list03,
                                  to_cover_flights_list04, to_cover_flights_list05, to_cover_flights_list06,
                                  to_cover_flights_list07, to_cover_flights_list08, to_cover_flights_list09,
                                  to_cover_flights_list10, to_cover_flights_list11, to_cover_flights_list12]
