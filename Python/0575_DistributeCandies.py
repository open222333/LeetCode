class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))


candyType = [1, 1, 2, 2, 3, 3]
print(Solution().distributeCandies(candyType))
