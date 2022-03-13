class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binary_to_decimal(target):
            stock = 0
            count = 1
            for num in target:
                digit = len(target) - count
                stock += int(num) * (2 ** digit)
                count += 1
            return stock
        return bin(binary_to_decimal(a) + binary_to_decimal(b)).replace("0b", "")


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # https://leetcode.com/problems/add-binary/discuss/847720/Super-Simple-Python-Solution-1-Line
        return bin(int(a, 2)+int(b, 2))[2:]


a = "11"
b = "1"
print(Solution().addBinary(a, b))
