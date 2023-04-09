class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1

        left = 0
        right = x

        while left < right:
            mid = (left + right) // 2
            if mid * mid == x:
                return int(mid)
            elif mid * mid < x < (mid + 1) * (mid + 1):
                return int(mid)
            elif (mid + 1) * (mid + 1) == x:
                return int(mid + 1)
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1

        return int(right)


class Solution2:
    '''https://leetcode.com/problems/sqrtx/solutions/2401150/python-solution/?q=python&orderBy=most_relevant'''

    def mySqrt(self, x: int) -> int:
        sr = 1
        while True:
            if x < sr * sr:
                return sr - 1
            else:
                sr += 1


class Solution3:
    '''
    Binary Search
    https://leetcode.com/problems/sqrtx/solutions/1995489/python-98-easy-binary-search/?q=python&orderBy=most_relevant'''

    def mySqrt(self, x: int) -> int:
        from math import trunc

        if x == 1:
            return 1

        left = 0
        right = x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return trunc(right)


class Solution3(object):
    '''https://leetcode.com/problems/sqrtx/solutions/167547/python-solution/?q=python&orderBy=most_relevant'''

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        def bSearch(x):
            i = 0
            j = x
            while i < j:
                mid = (i + j) / 2
                res = mid ** 2
                nex = (mid + 1) ** 2
                if res == x:
                    return mid
                elif nex == x:
                    return mid + 1
                elif res < x < nex:
                    return mid
                elif x < res:
                    j = mid - 1
                else:
                    i = mid + 1
            return i
        if x == 1:
            return 1
        return bSearch(x)
