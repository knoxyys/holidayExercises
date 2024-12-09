#  This chapter is intentionally short, because when you finish these exercises, you should revisit your previous programs and see how functions can improve the organization of those programs as well (gulp)

print("Enter two strings and I'll tell you if they are anagrams: ")
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

def isAnagram(word1, word2):
    if set(word1) == set(word2) and len(word1) == len(word2): # set ignores order of items but ignores duplication, len fixes this
        return True
    else: return False
    
if isAnagram(s1, s2) == True:
    print(f"{s1} and {s2} are anagrams.")
else: print(f"{s1} and {s2} are not anagrams.")