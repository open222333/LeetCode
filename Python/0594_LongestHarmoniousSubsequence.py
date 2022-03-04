# Approach 1: Brute Force
# Approach 2: Better Brute Force
# Approach 3: Using Sorting
# Approach 4: Using HashMap
# Approach 5: In Single Loop
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Approach 4: Using HashMap
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        ans = 0
        for key in hashmap.keys():
            if key + 1 in hashmap:
                ans = max(ans, hashmap[key] + hashmap[key + 1])
        return ans


nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(Solution().findLHS(nums))
