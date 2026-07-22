import csv
with open('../csv/employees.csv', 'r') as file:
    reader = csv.reader(file)
    row_list = []
    for row in reader:
        row_list.append(row)

print(row_list)

name_list = [x[0] + " " + x[1] for x in row_list[1:]]
print(name_list)

e_names_list = [name for name in name_list if 'e' in name]
print(e_names_list)

