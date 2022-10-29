// Quick Question #1
// new Set([1,1,2,2,3,4])  // {1,2,3,4}

// Quick Question #2
// [...new Set("referee")].join("") // "ref"

// Quick Question #3
// let m = new Map();
// m.set([1,2,3], true);
// m.set([1,2,3], false);
// Answer:
// 0: {Array(3) => true}
// 1: {Array(3) => false}

// hasDuplicate
const hasDuplicate = (arr) => new Set(arr).size !== arr.length;

// vowelCount
const vowelCount = (str) => {
  const vowelMap = new Map();
  const lowerStr = str.toLowerCase();
  for (let char of lowerStr) {
    if ("aeiou".includes(char)) {
      if (vowelMap.has(char)) {
        vowelMap.set(char, vowelMap.get(char) + 1);
      } else {
        vowelMap.set(char, 1);
      }
    }
  }
  return vowelMap;
};
