"use strict";
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
function isAnagram(s, t) {
    if (s.length !== t.length)
        return false;
    let first = s.split("");
    const second = t.split("");
    for (let i = 0; i < first.length; i++) {
        const element = second[i];
        let found = first.indexOf(element);
        if (found == -1) {
            return false;
        }
        first[found] = null;
    }
    return true;
}
const eg1 = "anagram";
const eg2 = "nagaram";
console.log(isAnagram(eg1, eg2));
console.log(isAnagram("cat", "rat"));
//# sourceMappingURL=validAnagram.js.map