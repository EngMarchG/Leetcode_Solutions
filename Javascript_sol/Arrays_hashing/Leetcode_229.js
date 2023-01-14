/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
  let tt = parseInt(nums.length/3);
  let hmap = {};
  let arr = [];

  nums.forEach((num, ind) => {
      if (hmap[num]) {
          hmap[num] += 1
      } else {hmap[num] = 1};
      if (hmap[num]>tt) {
          arr.push(num)
      }
  });
  arr = Array.from(new Set(arr))
  return arr
};