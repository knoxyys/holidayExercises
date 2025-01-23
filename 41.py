names = [
    ('Ling', 'Mai'),
    ('Johnson', 'Jim'),
    ('Zarnecki', 'Sabrina'),
    ('Jones', 'Chris'),
    ('Jones', 'Aaron'),
    ('Swift', 'Geoffrey'),
    ('Xiong', 'Fong'),
]

def get_firstname(entry):
    return entry[1]

names_sorted = sorted(names, key = get_firstname)

with open ("41output.txt", "w") as hi:
    print(f"Total of {len(names)} names\n-----------------", file=hi)
    for last, first in names_sorted:
        print(f"{last}, {first}", file=hi)