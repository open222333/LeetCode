'''
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
import re


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = re.search(r'{}'.format(needle), haystack)
        if result:
            return result.start()
            # return result.span()[0]
        else:
            return -1


# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/3257529/python-short-and-clean-5-different-solutions-functional-programming/?languageTags=python3

class Solution1:
    '''Approach 1: Two pointers
    This is the standard brute force with two pointer approach.
    Usually haystack is so long that it doesn't fit in memory.
    These are called online input problems.
    The rest of the solutions assume this to be the case, and solve for generic cases.
    '''

    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if all(haystack[i + j] == needle[j] for j in range(len(needle))):
                return i
        return -1
