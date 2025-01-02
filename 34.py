employees = ['John Smith', 'Jackie Jackson', 'Chris Jones', 'Amanda Cullen', 'Jeremy Goodwin']

print(f"There are {len(employees)} employees: ")
print(*employees, sep = ', ')

name = input("Enter an employee name to remove: ")
if name in employees:
    employees.remove(name)

print(f"There are {len(employees)} employees: ")
print(*employees, sep = ', ')