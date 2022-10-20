/**
 * @param {number} num
 * @return {string}
 */
 var intToRoman = function(num) {
  let hmap = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'};
  let total = '';
  let temp = 0;
  
  // A list in decending order is necessary since js sorts keys by ascending order
  // It is more efficient to just manually create the list your self in this case
  Object.keys(hmap).sort(function(a, b){return b-a}).forEach((ele) => {
      temp = parseInt(num / ele);
      if (temp > 0) {
          total += hmap[ele].repeat(temp);
          num = num % ele;
      };
  });
  return total
};