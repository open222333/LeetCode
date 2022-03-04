# Approach #1 Single Scan [Accepted]
# Approach #2 Optimized [Accepted]
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        max_place = 0
        flowerbed.insert(0, 0)
        flowerbed.append(0)

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i + 1] != 1 and flowerbed[i - 1] != 1:
                flowerbed[i] = 1
                max_place += 1
        return n <= max_place


# flowerbed = [1, 0, 0, 0, 1]
# flowerbed = [1, 0, 0, 0, 0, 1]
flowerbed = [0, 0, 1, 0, 1]
n = 1
print(Solution().canPlaceFlowers(flowerbed, n))
