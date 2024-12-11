def returnPassword(pword):
    if len(pword) < 8:
        if pword.isnumeric() == True: # check for only numbers
            return "very weak"
        else:
            return "weak"
    else:
        if pword.isnumeric() or pword.isalpha() == True:
            return "alright" # had to make up some cases where a concrete definition wasn't given
        else:
            chars = 0
            for i in range(len(pword)):
                if pword[i].isnumeric() or pword[i].isalpha() == True:
                    chars = chars + 1 # counter for alphanumeric characters
            if len(pword) == chars:
                return "strong"
            else: return "very strong"

password = input("Enter password: ")
result = returnPassword(password)
print(f"The password '{password}' is a {result} password.")