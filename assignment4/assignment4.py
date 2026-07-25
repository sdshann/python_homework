import pandas as pd

#Task 1
data = {
    "Name": ['Alice', 'Bob', 'Charlie'],
    "Age": [25, 30, 35],
    "City": ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)

task1_data_frame = df
task1_with_salary = df.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print(task1_older)

task1_older.to_csv("employees.csv", index=False)

#Task 2
df = pd.read_csv('employees.csv')
task2_employees = df
print(task2_employees)

df = pd.read_json('additional_employees.json')
json_employees = df 
print(json_employees)

df = pd.concat([task2_employees, json_employees], ignore_index=True)
more_employees = df
print(more_employees)

#Task 3
first_three = more_employees.head(3)
print(first_three)

last_two = more_employees.tail(2)
print(last_two)

employee_shape = more_employees.shape
print(employee_shape)

more_employees.info()

#Task 4
df = pd.read_csv('dirty_data.csv')
dirty_data = df
clean_data = dirty_data.copy()
clean_data = clean_data.drop_duplicates()
print(clean_data)
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")

clean_data["Salary"] = clean_data["Salary"].replace("unknown", pd.NA)
clean_data["Salary"] = clean_data["Salary"].replace("n/a", pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print(clean_data)

mean_age = clean_data["Age"].mean()
clean_data["Age"] = clean_data["Age"].fillna(mean_age)
median_salary = clean_data["Salary"].median()
clean_data["Salary"] = clean_data["Salary"].fillna(median_salary)
print(clean_data)

clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], format='mixed', errors="coerce")
print(clean_data)

clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Department"] = clean_data["Department"].str.strip()
clean_data["Name"] = clean_data["Name"].str.upper()
clean_data["Department"] = clean_data["Department"].str.upper()
print(clean_data)