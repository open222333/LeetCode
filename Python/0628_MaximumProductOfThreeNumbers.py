# Approach 1: Brute Force
# Approach 2: Using Sorting
# Approach 3: Single Scan
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Approach 2: Using Sorting
        # 一個數是最大正數 其餘兩個數可能可以是負數 (Time Limit Exceeded)
        first_num = max(nums)
        nums.remove(first_num)
        nums.sort()
        if first_num > 0:
            return max(first_num * nums[len(nums) - 2] * nums[len(nums) - 1], first_num * nums[0] * nums[1])
        elif first_num < 0:
            return first_num * nums[len(nums) - 2] * nums[len(nums) - 1]
        else:
            return 0


# nums = [1, 2, 3]
# nums = [-100, -98, -1, 2, 3, 4]
nums = [-1, -2, -3, -4]
print(Solution().maximumProduct(nums))
