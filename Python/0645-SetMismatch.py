# Approach 1: Brute Force
# Approach 2: Better Brute Force
# Approach 3: Using Sorting
# Approach 4: Using Map
# Approach 5: Using Extra Array
# Approach 6: Using Constant Space
# Approach 7: Using XOR
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 自己的解法
        map_dict = {}
        for i in range(1, len(nums) + 1):
            map_dict[i] = 0
        for num in nums:
            map_dict[num] += 1
        for key in map_dict.keys():
            if map_dict[key] == 0:
                value_absence = key
            elif map_dict[key] == 2:
                value_duplicacy = key
            else:
                pass
        return [value_duplicacy, value_absence]

    def findErrorNums2(self, nums: List[int]) -> List[int]:
        # https://leetcode.com/problems/set-mismatch/discuss/387231/Python-98.80-super-easy-math
        # 數學解法
        # https://zh.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%80%A6
        n = len(nums)
        s = n * (n + 1) // 2  # 自然數總和
        absence = s - sum(set(nums)) # 找出遺失的
        # duplicacy = sum(nums) - sum(set(nums))
        duplicacy = sum(nums) + absence - s
        return [duplicacy, absence]


nums = [1, 2, 2, 4]
print(Solution().findErrorNums2(nums))
