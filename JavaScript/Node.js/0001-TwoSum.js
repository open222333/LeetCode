/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  for (i = 0; i < nums.length; i++) {
    diff = target - nums[i]
    for (j = i + 1; j < nums.length; j++) {
      if (nums[j] === diff) {
        return [i, j]
      }
    }
  }
};

nums = [2, 7, 11, 15]
target = 9
console.log(twoSum(nums, target))