/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
  nums.sort((a,b) => a-b);
  for (let i=0; i < nums.length-1; i++) {
      if (nums[i] === nums[i+1]) {
          return nums[i];
      }
  };
};


// Using Floyd's Tortoise and Hare (Cycle Detection)
/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
  let slow = nums[0]
  let fast = nums[0]

  while (true) {
      slow = nums[slow]
      fast = nums[nums[fast]]
      if (slow == fast) break
  }
  slow = nums[0]
  while (slow != fast) {
      slow = nums[slow]
      fast = nums[fast]
  }

  return slow
};