# 最長連續遞增子序列


from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # Approach #1: Sliding Window [Accepted]
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i - 1] >= nums[i]:
                '''
                i = 0 false
                nums[i - 1] >= nums[i]如果下一個比較小 True 因此非遞增子序列 更改anchor
                '''
                anchor = i
            print(f"ans:{ans}\ni:{i}\nanchor:{anchor}\n")
            ans = max(ans, i - anchor + 1)
        return ans


nums = [1, 3, 5, 4, 7]
# nums = [2,2,2,2,2]
print(Solution().findLengthOfLCIS(nums))
