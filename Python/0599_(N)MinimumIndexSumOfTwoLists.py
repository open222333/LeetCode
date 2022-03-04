# Approach #1 Using HashMap [Accepted]
# Approach #2 Without Using HashMap [Accepted]
# Approach #3 Using HashMap (linear) [Accepted]
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    ans[list1[i]] = i + j
        return [z[0] for z in sorted(ans.items())]

    def findRestaurant2(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        sum = len(list1) + len(list2)
        for i in range(sum):
            for j in range(sum):
                if j < len(list1) and sum - j < len(list2) and list1[j] == list2[sum - j]:
                    res.append(list1[i])
        return res


# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# list2 = ["KNN", "KFC", "Burger King", "Tapioca Express", "Shogun"]
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
print(Solution().findRestaurant2(list1, list2))
