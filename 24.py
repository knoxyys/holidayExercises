#  This chapter is intentionally short, because when you finish these exercises, you should revisit your previous programs and see how functions can improve the organization of those programs as well (gulp)

def isAnagram(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    else: return False

print("Enter two strings and I'll tell you if they are anagrams: ")
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
   
if isAnagram(s1, s2) == True:
    print(f"{s1} and {s2} are anagrams.")
else: print(f"{s1} and {s2} are not anagrams.")