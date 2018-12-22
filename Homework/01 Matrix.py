import collections
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(matrix)
        col = len(matrix[0])
        newMatrix = [[float('inf') for i in range(col)] for i in range(row)]

        queue = collections.deque()
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    newMatrix[i][j] = 0
                    queue.append((i,j))
        
        while queue:
            (r, c) = queue.popleft()
            for (move0, move1) in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                newR, newC = r + move0, c + move1
                if 0 <= newR < row and 0 <= newC < col and newMatrix[r][c] + 1 < newMatrix[newR][newC]:
                    newMatrix[newR][newC] = newMatrix[r][c] + 1
                    queue.append((newR, newC))

        return newMatrix

matrix = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]
test = Solution()
print(test.updateMatrix(matrix))