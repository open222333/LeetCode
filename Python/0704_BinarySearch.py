from typing import List

# Approach 1: Binary Search


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_node = 0
        right_node = len(nums) - 1

        while left_node <= right_node:

            # 取中間元素
            pivot = left_node + (right_node - left_node) // 2

            if nums[pivot] == target:
                return pivot

            if nums[pivot] < target:
                left_node = pivot + 1
            else:
                right_node = pivot - 1
        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(Solution().search(nums, target))
