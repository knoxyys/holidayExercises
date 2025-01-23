last_upper = 0
first_upper = 0

last_gap = ''
first_gap = ''
dashes = '---------------'

with open('42input.csv', mode ='r') as hi:
    for line in hi:
        values = line.strip().split(',')
        lastname = values[0]
        firstname = values[1]
        
        if len(lastname) > last_upper:
            last_upper = len(lastname)
        if len(firstname) > first_upper:
            first_upper = len(firstname)
    
    for i in range(last_upper):
        last_gap += ' '
        dashes += '-'
    for i in range(first_upper):
        first_gap += ' '
        dashes += '-'
    
    print(f"Last{last_gap}First{first_gap}Salary\n{dashes}")
    
    hi.seek(0) # this is stupid
    
    for line in hi:
        values = line.strip().split(',')
        print(f"{values[0]:<{last_upper}}    {values[1]:<{first_upper}}     {values[2]}")