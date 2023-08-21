`Given two strings s and t, 
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

`;

function isAnagram(s: string, t: string): boolean {
  // checking the length of the string,
  // if they don't have the same length they can't be anagram
  if (s.length !== t.length) return false;

  //   converting the string into an array with split method
  let first: Array<string | null> = s.split("");
  const second = t.split("");

  //   creating a loop through the array
  for (let i = 0; i < first.length; i++) {
    // go through second array and assign
    // value of element from second array
    const element = second[i];

    // check the index of element in first array
    let found = first.indexOf(element);

    // if element doesn't exist then return false
    if (found == -1) {
      return false;
    }

    // if element exists then remove it from first array
    first[found] = null;
  }

  return true;

  //   time complexity = 0(n^2)
  //   space complexity = 0(n)
}

const eg1 = "anagram";
const eg2 = "nagaram";

console.log(isAnagram(eg1, eg2));
console.log(isAnagram("cat", "rat"));
