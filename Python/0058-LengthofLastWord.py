# 58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = ''
        str_list = s.split(' ')
        for i in range(len(str_list)):
            if str_list[i] != '':
                ans = str_list[i]
        return len(ans)


s = Solution()
a = s.lengthOfLastWord(s="   fly me   to   the moon  ")
print(a)
