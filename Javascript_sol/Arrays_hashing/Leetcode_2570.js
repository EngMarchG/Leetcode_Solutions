/**
 * @param {number[][]} nums1
 * @param {number[][]} nums2
 * @return {number[][]}
 */
var mergeArrays = function(nums1, nums2) {
  var obj = {}
  let p1 = 0
  let p2 = 0
  
  while (p1 < nums1.length || p2 < nums2.length) {
          if (p1 < nums1.length) {
              if (!obj[nums1[p1][0]]) {
              obj[nums1[p1][0]] = nums1[p1][1]
          } else {
          obj[nums1[p1][0]] += nums1[p1][1]
          }
          p1++}

          if (p2 < nums2.length) {
              if (!obj[nums2[p2][0]]) {
              obj[nums2[p2][0]] = nums2[p2][1]
          } else {
              obj[nums2[p2][0]] += nums2[p2][1]
          }
           p2++ }
      }


  const result = [];
  for (const [key, value] of Object.entries(obj)) {
      result.push([parseInt(key), value]);
  }
  return result;
};