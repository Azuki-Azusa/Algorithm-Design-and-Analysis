class Solution:
    post = []
    keep = []
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                if "O" == board[i][j]:
                    if self.DFS(i, j, board):
                        self.keep = self.keep + self.post
                    self.post.clear()
        for [i,j] in self.keep:
            board[i][j] = "O"

    def DFS(self, i, j, board):
        self.post.append([i,j])
        board[i][j] = "X"
        
        flag = False
        if i > 0 and "O" == board[i-1][j]:
            temp = self.DFS(i-1, j, board)
            flag = temp or flag
        if i < len(board)-1 and "O" == board[i+1][j]:
            temp = self.DFS(i+1, j, board)
            flag = temp or flag
        if j > 0 and "O" == board[i][j-1]:
            temp = self.DFS(i, j-1, board)
            flag = temp or flag
        if j < len(board[i])-1 and "O" == board[i][j+1]:
            temp = self.DFS(i, j+1, board)
            flag = temp or flag
        if i == 0 or i == len(board)-1 or j == 0 or j == len(board[i]) - 1:
            flag = True
        return flag

'''
test = Solution()
board = [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]
test.solve(board)
print(board)
'''

