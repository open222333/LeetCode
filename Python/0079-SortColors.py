from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

nums = [2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums)