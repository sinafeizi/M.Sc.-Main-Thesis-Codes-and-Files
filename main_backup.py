import sys
from functions import is_arced_arrow
from functions import ds_algorithm
from functions import get_cost
sys.setrecursionlimit(1000000000)
f = open("19690.txt", "r")
flights_list = f.readlines()
f.close()
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
slp = []
child_flights = []
children = []
for i in matrix:
    i.append(children)
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if is_arced_arrow(matrix[i], matrix[j]):
            matrix[i].append(j)
for i in range(len(matrix)):
    matrix[i][6] = matrix[i][7:]
for i in matrix:
    tool = len(i) - 7
    for j in range(tool):
        i.pop()
stacks_dic = {}
base_cities = ["13830", "12173"]
for f in matrix:
    if f[0] in base_cities:
        ds_algorithm(f, matrix, [f], slp, 0, stacks_dic)
for d in slp:
    d.append(get_cost(d))
covered_flights_list = []
for ff in matrix:
    for pp in slp:
        if ff in pp:
            if ff not in covered_flights_list:
                covered_flights_list.append(ff)
print(len(slp))
print(len(matrix))
print(len(covered_flights_list))
for ii in range(len(slp)):
    for jj in range(len(slp[ii]) - 1):
        slp[ii][jj] = slp[ii][jj][:-1]
for iii in range(len(covered_flights_list)):
    covered_flights_list[iii] = covered_flights_list[iii][:-1]
new_file1 = open("all_flights_158_lines.txt", "w")
for kk in covered_flights_list:
    new_file1.write(str(kk))
    new_file1.write("\n")
new_file1.close()
new_file2 = open("all_pairings_706_lines.txt", "w")
for kkk in slp:
    new_file2.write(str(kkk))
    new_file2.write("\n")
new_file2.close()
