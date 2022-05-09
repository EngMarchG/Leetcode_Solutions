/**
 * @param {number[]} nums
 * @return {boolean}
 */
// Optimal Solution: check if the length of the Set of the array 
// is equal to the length of the array
// Time complexity: O(nums.length); Space complexity: O(num.length)
 var containsDuplicate = function(nums) {
    nums2 = [...new Set(nums)]
    if (nums.length === nums2.length) {
        return false
    }
    return true
};




/**
 * @param {number[]} nums
 * @return {boolean}
 */

// Time complexity: O(nums.length); Space complexity: O(num.length)
// Hashmap each value of the array and if it already exists return true
var containsDuplicate = function(nums) {
    let uniq = {};
    let ans = false;
    for (i=0; i<=nums.length; i++) {
        if (uniq[nums[i]] != undefined) {
            ans = true;
            break;
            
        } else {
            uniq[nums[i]] = 1;
        } 
    }
    return ans;
}