import re

def textValidate(x):
    if x == '': # if empty, not fully alphabetical or shorter than 2 characters then return false
        return "The name field must be filled in."
    elif len(x) < 2:
        return f"{x} is not a valid name. It is too short."
    elif not x.isalpha():
        return "The name field must be alphabetical."
    return True

def idValidate(x):
    if re.fullmatch(r"^[A-Z]{2}-\d{4}$", x): # if two uppercase letters, then hyphen, then four digits then return true (https://docs.python.org/3/library/re.html)
        return True
    return f"{x} is not a valid ID."

def zipValidate(x):
    if x.isdigit(): # if zip is alll numerical return true (this is stupid isdigit works but not isnumerical)
        return True
    return "The ZIP code must be numeric."
    
def validateInput(w, x, y, z):
    output = []
    functions = [textValidate(w), textValidate(x), idValidate(y), zipValidate(z)]
    for i in range(4):
        if functions[i] != True:
            output.append(functions[i])
    if output:
        return "\n".join(output) # joins items in list with new line
    else: return "There were no errors found."

first = input("Enter the first name: ")
last = input("Enter the last name: ")
zip = input("Enter the ZIP code: ")
id = input("Enter an employee ID: ")

print(validateInput(first, last, id, zip))