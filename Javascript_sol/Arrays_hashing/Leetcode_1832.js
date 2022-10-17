/**
 * @param {string} sentence
 * @return {boolean}
 */
// Not the intended solution 
// Time complexity O(N) Space complexity O(set(N))
 var checkIfPangram = function(sentence) {
  if (new Set(sentence).size === 26) {
      return true
  };
  return false
};



/*
// Time complexity O(N + set(N)) Space complexity O(set(N))
 var checkIfPangram = function(sentence) {
  var hmap = {};
  Array.from(sentence).forEach((letter) => {
     if (hmap.hasOwnProperty(letter) === false) {
         hmap[letter] = 1
     };
  });
  
  if (Object.keys(hmap).length === 26) {
      return true
  }
  return false
};
*/