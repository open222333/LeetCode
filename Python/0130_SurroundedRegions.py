from typing import List


'''
depth first search 深度搜尋 演算法 應用

像圍棋規則

https://leetcode.com/problems/surrounded-regions/discuss/475014/python3-BFS-and-DFS
1. 將所有跟邊界相連的O都更換成N
2. 將所有O都更換成X
3. 將N更換成O
'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Runtime Error
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board[0]), len(board)
        if R <= 2 or C <= 2:
            return

        # 將邊界的O變成N
        for r in range(R):
            self.depthFirstSearch(board, r, 0, R, C)
            self.depthFirstSearch(board, r, C - 1, R, C)

        for c in range(C):
            self.depthFirstSearch(board, 0, c, R, C)
            self.depthFirstSearch(board, R - 1, c, R, C)

        # 將所有O都更換成X 將N更換成O
        for r in range(R):
            for c in range(C):
                if board[c][r] == 'O':
                    board[c][r] = 'X'
                if board[c][r] == 'N':
                    board[c][r] = 'O'

    def depthFirstSearch(self, board, r, c, R, C):
        '''深度搜尋 將相鄰的O都變成N
        r:第幾列
        c:第幾欄
        R:最大列數量
        C:最大欄數量
        '''
        if 0 <= r < R and 0 <= c < C and board[c][r] == 'O':
            board[c][r] = 'N'
            self.depthFirstSearch(board, r + 1, c, R, C)
            self.depthFirstSearch(board, r - 1, c, R, C)
            self.depthFirstSearch(board, r, c + 1, R, C)
            self.depthFirstSearch(board, r, c - 1, R, C)


class Solution1:

    '''
    recursion, dfs
    '''

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        R, C = len(board), len(board[0])
        if R <= 2 or C <= 2:
            return

        # start from the boarder and replace all O to N
        # put all the boarder value into queue.
        for r in range(R):
            self.dfs(board, r, 0, R, C)
            self.dfs(board, r, C-1, R, C)

        for c in range(C):
            self.dfs(board, 0, c, R, C)
            self.dfs(board, R-1, c, R, C)

        # replace all the O to X, then replace all the N to O
        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "N":
                    board[r][c] = "O"

    def dfs(self, board, r, c, R, C):
        '''depth first search 深度搜尋 演算法'''
        if 0 <= r < R and 0 <= c < C and board[r][c] == "O":
            board[r][c] = "N"
            self.dfs(board, r, c+1, R, C)
            self.dfs(board, r, c-1, R, C)
            self.dfs(board, r-1, c, R, C)
            self.dfs(board, r+1, c, R, C)


# board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
# board = [["O", "X", "X", "O", "X"], ["X", "O", "O", "X", "O"], [
#     "X", "O", "X", "O", "X"], ["O", "X", "O", "O", "O"], ["X", "X", "O", "X", "O"]]
board = [["X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X"],
         ["X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X"]]
Solution().solve(board)
print(board)


# ["O","X","X","O","X"]
# ["X","O","O","X","O"]
# ["X","O","X","O","X"]
# ["O","X","O","O","O"]
# ["X","X","O","X","O"]

# ["O","X","X","O","X"]
# ["X","X","X","X","O"]
# ["X","X","X","X","X"]
# ["O","X","X","X","O"]
# ["X","X","O","X","O"]
