"""Given two strings s and t, 
return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original 
letters exactly once.


example 1:
Input: s = 'anagram' t='nagaram'
Output: true

example 2:
Input: s = 'rat' t='cat'
Output: true
"""

def isAnagram(s: str, t: str) -> bool:
    # Checking the length of the strings,
    # if they don't have the same length they can't be anagrams
    if len(s) != len(t):
        return False

    # Converting the strings into arrays using split method
    first = list(s)
    second = list(t)


    # Creating a loop through the array
    for i in range(len(first)):
        # Getting the element from the second array
        element = second[i]

       
        try:

        # Check the index of the element in the first array
            found = first.index(element) 

        # If element doesn't exist in first array, return False
        except ValueError:
            return False



        # If element exists, remove it from the first array
        first[found] = None

    return True

# Test cases
print(isAnagram("anagram", "nagaram"))  # Output: True
print(isAnagram("rat", "car"))  # Output: False



