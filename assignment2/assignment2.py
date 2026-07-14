#Task 2
import csv

from numpy import sort

def read_employees():
    employee_dict = {}
    row_list = []
    first_row = True
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if first_row:
                    employee_dict['fields'] = row
                    first_row = False
                else:
                    row_list.append(row)                
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    employee_dict['rows'] = row_list
    return employee_dict

employees = read_employees()
print(employees)

#Task 3
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")
print(employee_id_column)

#Task 4
def first_name(row_number):
    return employees["rows"][row_number][column_index("first_name")]

#Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

#Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

#Task 7
def sort_by_last_name():
    employees["rows"].sort(key = lambda row: row[column_index("last_name")])
    return employees["rows"]

sort_by_last_name()
print(employees)

#Task 8
def employee_dict(row):
    new_dict = {}
    for i in range(len(employees["fields"])):
        if i == employee_id_column:
            continue
        new_dict[employees["fields"][i]] = row[i]
    return new_dict
print(employee_dict(employees["rows"][0]))

#Task 9
def all_employees_dict():
    combined_dict = {}
    for row in employees["rows"]:
        combined_dict[row[employee_id_column]] = employee_dict(row)
    return combined_dict
print(all_employees_dict())

#Task 10
import os
def get_this_value():
    return os.environ.get("THISVALUE")

#Task 11
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
set_that_secret("pineapple!")

print(custom_module.secret)

#Task 12
def read_csv_file(file_name):
    minutes_dict = {}
    row_list = []
    first_row = True
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if first_row:
                    minutes_dict['fields'] = row
                    first_row = False
                else:
                    row_list.append(tuple(row))                
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    minutes_dict['rows'] = row_list
    return minutes_dict

def read_minutes():
    minutes1 = read_csv_file('../csv/minutes1.csv')
    minutes2 = read_csv_file('../csv/minutes2.csv')
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1, minutes2)

#Task 13
def create_minutes_set():
    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])
    combined_set = set1.union(set2)
    return combined_set
    
minutes_set = create_minutes_set()

#Task 14
from datetime import datetime
def create_minutes_list():
    converted_minutes_list = list(minutes_set)
    minutes_tuple = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), converted_minutes_list))
    return minutes_tuple
minutes_list = create_minutes_list()
print(minutes_list)

#Task 15
def write_sorted_list():
    minutes_list.sort(key = lambda x: x[1])
    sorted_tuple = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))
    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(sorted_tuple)
    return sorted_tuple