from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        '''Time Limit Exceeded'''
        array = []

        # 建立初始表
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(0)
            array.append(temp)

        # 進行數字加總
        for addnumlist in ops:
            for i in range(addnumlist[0]):
                for j in range(addnumlist[1]):
                    array[i][j] += 1

        # 建立hashmap
        hashmap = {}
        for i in range(m):
            for j in range(n):
                if array[i][j] not in hashmap:
                    hashmap[array[i][j]] = 1
                else:
                    hashmap[array[i][j]] += 1
        return hashmap[max(hashmap.keys())]

    def maxCount2(self, m: int, n: int, p: List[List[int]]) -> int:
        # https://leetcode.com/problems/range-addition-ii/discuss/380432/Solution-in-Python-3-(one-line)-(beats-~98)
        # p = 0 -> false
        # 取最小 因為最小值會加最多次
        # Python 三元表達式：
        # if p:
        #     ans = min([i[0] for i in p]) * min(i[1] for i in p)
        # else:
        #     ans = m * n
        # return ans
        return min([i[0] for i in p]) * min(i[1] for i in p) if p else m * n


m = 3
n = 3
ops = [[2, 2], [3, 3]]
print(Solution().maxCount2(m, n, ops))
