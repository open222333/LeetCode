class Solution:
    def climbStairs(self, n: int) -> int:
        '''費氏數列
        f(n) = f(n - 1) + f(n - 2)
        https://www.youtube.com/watch?v=Y0lT9Fck7qI&t=3s&ab_channel=NeetCode'''
        one, two = 1, 1
        for _ in range(n - 1):
            temp = one + two
            one = two
            two = temp
        return two

    def climbStairs2(self, n: int) -> int:
        one, two = 1, 1
        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
