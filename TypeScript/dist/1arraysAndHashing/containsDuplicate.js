"use strict";
`given an integer array nums, return true if any value appears 
at least twice in the array and return false if every 
element is distinct

EG :
Input: nums= [1,2,3,1]
Output: true 

Input: nums= [1,2,3,4]
Output: false

Input: nums= [1,1,1,2,3,2,4,3,2,4,1]
Output: true 




time complexity--> O(n^2) --> we have to compare every elements to the rest of the elements in the array
space complexity--> O(1) --> we don't need extra memory
`;
`
// creating a function that takes array of numbers and return boolean
function containsDuplicate(nums: number[]): boolean {
  // creating a new set (set is a collection of unique values)
  const set = new Set();
  // creating a loop
  for (let i = 0; i < nums.length; i++) {
    // checks the value is already in set if it is then it returns true
    if (set.has(nums[i])) return true;
    // otherwise add that value to set
    else set.add(nums[i]);
  }
  // if duplicate value doesn't exist they return false
  return false;
}

console.log(containsDuplicate([1, 5, 7, 8, 6]));
console.log(containsDuplicate([1, 5, 7, 8, 6, 5, 5, 8, 6, 1, 2]));
console.log(containsDuplicate([1, 5, 7, 8, 6, 5, 0, 1, 2]));
`;
`
function containsDuplicate(nums: number[]): boolean {
  const numSet: Set<number> = new Set();

  for (const num of nums) {
    if (numSet.has(num)) {
      return true;
    }
    numSet.add(num);
  }

  return false;
}

// Example usages
const nums1: number[] = [1, 2, 3, 1];
console.log(containsDuplicate(nums1)); // Output: true

const nums2: number[] = [1, 2, 3, 4];
console.log(containsDuplicate(nums2)); // Output: false

const nums3: number[] = [1, 1, 1, 2, 3, 2, 4, 3, 2, 4, 1];
console.log(containsDuplicate(nums3)); // Output: true
`;
function containsDuplicate(nums) {
    nums.sort();
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === nums[i - 1]) {
            return true;
        }
    }
    return false;
}
//# sourceMappingURL=containsDuplicate.js.map