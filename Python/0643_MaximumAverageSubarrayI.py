# Approach #1 Cumulative Sum [Accepted]
# Approach #2 Sliding Window [Accepted]
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Time Limit Exceeded
        ans = 0
        if len(nums) == 1:
            ans = nums[0] / k
        else:
            for i in range(len(nums) - (k - 1)):
                ans = max(ans, sum([nums[j] for j in range(i, i + k)]) / k)
        return ans

    def findMaxAverage2(self, nums: List[int], k: int) -> float:
        # https://leetcode.com/problems/maximum-average-subarray-i/discuss/336428/Solution-in-Python-3-(beats-100)
        pass

    def findMaxAverage3(self, nums: List[int], k: int) -> float:
        # Sliding Window
        # https://leetcode.com/problems/maximum-average-subarray-i/discuss/885250/Python-3-or-Sliding-Window-or-5-Lines-or-O(n)-Time-O(1)-Space
        window = sum_max = sum(nums[:k])
        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]  # 加下一個 減第一個
            sum_max = max(sum_max, window)
        return sum_max / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
# nums = [5]
# k = 1
# nums = [0, 1, 1, 3, 3]
# k = 4
print(Solution().findMaxAverage3(nums, k))
