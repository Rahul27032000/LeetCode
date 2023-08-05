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
function containsDuplicate(nums) {
    const set = new Set();
    for (let i = 0; i < nums.length; i++) {
        if (set.has(nums[i]))
            return true;
        else
            set.add(nums[i]);
    }
    return false;
}
console.log(containsDuplicate([1, 5, 7, 8, 6]));
console.log(containsDuplicate([1, 5, 7, 8, 6, 5, 5, 8, 6, 1, 2]));
console.log(containsDuplicate([1, 5, 7, 8, 6, 5, 0, 1, 2]));
//# sourceMappingURL=containsDublicste.js.map