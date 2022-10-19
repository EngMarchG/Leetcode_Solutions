/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
// Time complexity O(m+logN) Space complexity O(1)
 var searchMatrix = function(matrix, target) {
  var x = 0
  while (x < matrix.length) {
      if (matrix[x][matrix[0].length - 1] >= target) {
          break
      };
      ++x;
  };
  if (matrix.length === x) {return false};
  
  let left = 0;
  let right = matrix[0].length;
  let mid = 0;
  
  while (left < right) {
      mid = parseInt((left + right)/2);
      if (matrix[x][mid] === target) {
          return true;
      } else if (matrix[x][mid] > target) {
          right = mid;
      } else {
          left = mid + 1;
      };
  };
  return false
};