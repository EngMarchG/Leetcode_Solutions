/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
 var containsNearbyDuplicate = function(nums, k) {
  let hmap = {};
  
  nums.forEach((ele, pos) => {
     if (hmap[ele]) {
         if ((pos - hmap[ele][0]) <= k) {
             k = -1
         };
         hmap[ele][0] = pos;
     } else {
         hmap[ele] = [pos, pos];
     };
  });
  
  if (k === -1) {return true}
  return false
};