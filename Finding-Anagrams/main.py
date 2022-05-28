# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from pickletools import string1


def find_anagram(word, anagram):
    # [assignment] Add your code here

    return True


str1 = input("string1:")
str2 = input("string2:")

sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)

if sorted_str1 == sorted_str2:
    print("given strings are anagram")
else:
    print("given strings are not anagrams")

    