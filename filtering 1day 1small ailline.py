f = open("On_Time_On_Time_Performance_2017_1.csv", "r")
flights_list = f.readlines()
f.close()
matrix = []
out_file = []
for i in range(1, len(flights_list)):
    matrix.append(flights_list[i].split(","))
for j in range(1, len(matrix)):
    if int(matrix[j][1]) == 1 and int(matrix[j][2]) == 1 and int(matrix[j][3]) == 1 and int(matrix[j][7]) == 19790:
        out_file.append(matrix[j])
for m in range(len(out_file)):
    out_file[m][0] = out_file[m][11]
    out_file[m][1] = out_file[m][21]
    out_file[m][2] = out_file[m][3]
    out_file[m][3] = out_file[m][31]
    out_file[m][4] = out_file[m][40]
for n in out_file:
    tool = len(n) - 5
    for j in range(tool):
        n.pop()
for y in out_file:
    y[3] = y[3][1:3] + ":" + y[3][3:-1]
    y[4] = y[4][1:3] + ":" + y[4][3:-1]
counter = 0
for z in out_file:
    counter += 1
print(counter)
ff = open("medium_5.txt", "w")
for k in range(len(out_file)):
    for p in range(1):
        ff.write(out_file[k][p])
    ff.write("\n")
ff.close()
