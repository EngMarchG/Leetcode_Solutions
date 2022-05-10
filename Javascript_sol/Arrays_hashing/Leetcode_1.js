/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
// Find the difference between the current number and target
// Save the difference and its position in the hashmap
// If a term in the array is defined in the hashmap then it is the target
// Time Complexity: O(nums) ; Space Complexity: O(nums)
var twoSum = function(nums, target) {
    let hmap = {};
    let diff = 0;
    for (i = 0 ; i < nums.length ; i++) {
        diff = target - nums[i];
        if (hmap[nums[i]] === undefined) {
            hmap[diff] = i;
        } else {
            return [ hmap[nums[i]], i ];
        }
    }
};