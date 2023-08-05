"""given an integer array nums, return true if any value appears 
at least twice in the array and return false if every 
element is distinct

EG :
Input: nums= [1,2,3,1]
Output: true 

Input: nums= [1,2,3,4]
Output: false

Input: nums= [1,1,1,,2,3,2,4,3,2,4,1]
Output: true 




time complexity--> O(n^2) --> we have to compare evert elements to the rest of the elements in the array
space complexity--> O(1) --> we don't need extra memory


"""

# solved using class methods
'''
class Solution:
    def containsDuplicate(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# Example usages
solution = Solution()

nums1 = [1, 2, 3, 1]
print(solution.containsDuplicate(nums1))  # Output: True

nums2 = [1, 2, 3, 4]
print(solution.containsDuplicate(nums2))  # Output: False

nums3 = [1, 1, 1, 2, 3, 2, 4, 3, 2, 4, 1]
print(solution.containsDuplicate(nums3))  # Output: True
'''
# solved using function method

def containsDuplicate(nums):
    hashset= set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


print(containsDuplicate([1,5,3,4]))
print(containsDuplicate([1,5,3,4,14,4,5,7,5,4,6]))
print(containsDuplicate([1,1,1,1,1]))
print(containsDuplicate([1,2,3,4,5,6]))