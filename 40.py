people = [
    {"firstname": "John", "lastname": "Johnson", "position": "Manager", "sepdate": "2016-12-31"},
    {"firstname": "Tou", "lastname": "Xiong", "position": "Software Engineer", "sepdate": "2016-10-05"},
    {"firstname": "Michaela", "lastname": "Michaelson", "position": "District Manager", "sepdate": "2015-12-19"},
    {"firstname": "Jake", "lastname": "Jacobson", "position": "Programmer", "sepdate": ""},
    {"firstname": "Jacquelyn", "lastname": "Jackson", "position": "DBA", "sepdate": ""},
    {"firstname": "Sally", "lastname": "Weber", "position": "Web Developer", "sepdate": "2015-12-18"}
]

search = input("Enter a search string: ")

def get_lastname(entry):
    return entry["lastname"]

people_sort = sorted(people, key = get_lastname) # didnt specifically say to do this but it was shown in the example

for entry in people_sort:
    if search in entry['firstname'] or search in entry['lastname']:
        print(f"{search} found in {entry['firstname'] or entry['lastname']}")
        entry['found'] = 1


print("Results: ")
print("Name                 | Position             | Separation Date")
print("---------------------|----------------------|----------------")

for entry in people_sort:
    try:
        if entry['found'] == 1:
            fullname = f"{entry['firstname']} {entry['lastname']}"
            position = entry['position']
            sepdate = entry['sepdate']
            print(f"{fullname:<20} | {position:<20} | {sepdate:<20}")
    except KeyError:
        continue # ooooooo error handling (theres probably a nicer way to do this)