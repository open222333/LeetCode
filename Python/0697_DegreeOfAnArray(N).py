# Approach #1: Left and Right Index [Accepted]
'''
https://home.gamer.com.tw/artwork.php?sn=5021121
陣列的「度數」定義為其中出現最多次的元素
找到 nums 中可能的最短子陣列（連續）之長度，其中該子陣列之度數與 nums 的度數一樣。
'''
from typing import List


class Solution:
    def findShortestSubArray_1(self, nums: List[int]) -> int:
        # 自己的解法 失敗
        from collections import Counter
        ans = len(nums)
        nums_counts = Counter(nums)
        degree = max(nums_counts.values())
        for i in nums_counts.items():
            if i[1] == degree:
                left = nums.index(i[0])
                right = nums.index(i[0], left + 1)
                # print(nums[left:right + 1])
                if max(Counter(nums[left:right + 1]).values()) == degree:
                    ans = min(ans, right - left + 1)
        return ans

    def findShortestSubArray(self, nums: List[int]) -> int:
        right, left, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
        return ans


# nums = [1, 2, 2, 3, 1]
nums = [1, 2, 2, 3, 1, 4, 2]
print(Solution().findShortestSubArray_1(nums))
