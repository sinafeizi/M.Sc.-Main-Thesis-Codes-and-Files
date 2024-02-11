import xlsxwriter

f1 = open("results_ACO.txt", "r")
f2 = open("results_ACO_old.txt", "r")
f3 = open("results_GA.txt", "r")
f4 = open("results_GA_2018.txt", "r")
f5 = open("results_PSO.txt", "r")

aco_times = f1.readlines()
aco_old_times = f2.readlines()
ga_times = f3.readlines()
ga_2018_times = f4.readlines()
pso_times = f5.readlines()

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()

number_lines_1 = len(aco_times)
number_lines_2 = len(aco_old_times)
number_lines_3 = len(ga_times)
number_lines_4 = len(ga_2018_times)
number_lines_5 = len(pso_times)

matrix1 = []
matrix2 = []
matrix3 = []
matrix4 = []
matrix5 = []

for i1 in range(number_lines_1):
    matrix1.append(aco_times[i1].split(" "))
for i2 in range(number_lines_2):
    matrix2.append(aco_old_times[i2].split(" "))
for i3 in range(number_lines_3):
    matrix3.append(ga_times[i3].split(" "))
for i4 in range(number_lines_4):
    matrix4.append(ga_2018_times[i4].split(" "))
for i5 in range(number_lines_5):
    matrix5.append(pso_times[i5].split(" "))

for j2 in range(len(matrix1)):
    if len(matrix1[j2]) == 2:
        for j3 in range(len(matrix1[j2])):
            matrix1[j2][j3] = float(matrix1[j2][j3])

for j2 in range(len(matrix2)):
    if len(matrix2[j2]) == 2:
        for j3 in range(len(matrix2[j2])):
            matrix2[j2][j3] = float(matrix2[j2][j3])

for j2 in range(len(matrix3)):
    if len(matrix3[j2]) == 2:
        for j3 in range(len(matrix3[j2])):
            matrix3[j2][j3] = float(matrix3[j2][j3])

for j2 in range(len(matrix4)):
    if len(matrix4[j2]) == 2:
        for j3 in range(len(matrix4[j2])):
            matrix4[j2][j3] = float(matrix4[j2][j3])

for j2 in range(len(matrix5)):
    if len(matrix5[j2]) == 2:
        for j3 in range(len(matrix5[j2])):
            matrix5[j2][j3] = float(matrix5[j2][j3])


with xlsxwriter.Workbook('results_ACO.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, data in enumerate(matrix1):
        worksheet.write_row(row_num, 0, data)

with xlsxwriter.Workbook('results_ACO_old.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, data in enumerate(matrix2):
        worksheet.write_row(row_num, 0, data)

with xlsxwriter.Workbook('results_GA.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, data in enumerate(matrix3):
        worksheet.write_row(row_num, 0, data)

with xlsxwriter.Workbook('results_GA_2018.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, data in enumerate(matrix4):
        worksheet.write_row(row_num, 0, data)

with xlsxwriter.Workbook('results_PSO.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, data in enumerate(matrix5):
        worksheet.write_row(row_num, 0, data)
