from typing import List

'''九宮格 平均值 若超出範圍不列入計算'''


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # 自己的解法
        import copy
        img2 = copy.deepcopy(img)
        for i in range(len(img)):
            for j in range(len(img[i])):
                if i - 1 < 0:
                    r1 = 0
                else:
                    r1 = i - 1
                if i + 2 >= len(img):
                    r2 = len(img)
                else:
                    r2 = i + 2
                if j - 1 < 0:
                    c1 = 0
                else:
                    c1 = j - 1
                if j + 2 > len(img[i]):
                    c2 = len(img[i])
                else:
                    c2 = j + 2
                count = 0
                amount = 0
                for r in range(r1, r2):
                    for c in range(c1, c2):
                        amount += img[r][c]
                        count += 1
                # print(amount, count)
                img2[i][j] = int(amount / count)
        return img2


img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
print(Solution().imageSmoother(img))
