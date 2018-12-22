class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        m = len(word1)
        n = len(word2)

        table = [[0 for col in range(n+1)] for row in range(m+1)]

        for i in range(m+1):
            table[i][0] = i
        
        for j in range(n+1):
            table[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                table[i][j] = min(table[i-1][j] + 1, table[i][j-1] + 1, table[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1))

        return table[m][n]

test = Solution()
word1 = "intention"
word2 = "execution"
print(test.minDistance(word1, word2))