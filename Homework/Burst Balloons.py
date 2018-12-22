class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for l in range(2, n):
            for x in range(n - l):
                y = x + l
                for z in range(x + 1, y):
                    dp[x][y] = max(dp[x][y], nums[x] * nums[z] * nums[y] + dp[x][z] + dp[z][y])

        return dp[0][n - 1]

test = Solution()
nums = [3,1,5,8]
print(test.maxCoins(nums))