people = [
    {"firstname": "John", "lastname": "Johnson", "position": "Manager", "sepdate": "2016-12-31"},
    {"firstname": "Tou", "lastname": "Xiong", "position": "Software Engineer", "sepdate": "2016-10-05"},
    {"firstname": "Michaela", "lastname": "Michaelson", "position": "District Manager", "sepdate": "2015-12-19"},
    {"firstname": "Jake", "lastname": "Jacobson", "position": "Programmer", "sepdate": ""},
    {"firstname": "Jacquelyn", "lastname": "Jackson", "position": "DBA", "sepdate": ""},
    {"firstname": "Sally", "lastname": "Weber", "position": "Web Developer", "sepdate": "2015-12-18"}
]

def get_lastname(entry):
    return entry["lastname"]

people_sort = sorted(people, key = get_lastname)

print("Name                 | Position             | Separation Date")
print("---------------------|----------------------|-----------")

for entry in people_sort:
    fullname = f"{entry['firstname']} {entry['lastname']}"
    position = entry['position']
    sepdate = entry['sepdate']
    print(f"{fullname:<20} | {position:<20} | {sepdate:<15}")