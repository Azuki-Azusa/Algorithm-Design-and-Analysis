class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        n = len(stations)
        if startFuel >= target:
            return 0
        dp = [[0 for i in range(n + 1)] for i in range(n + 1)]

        dp[0][0] = startFuel


        for i in range(1, n + 1):
            if startFuel >= stations[i-1][0]:
                dp[i][0] = startFuel
        
        for j in range(1, n + 1):
            for i in range(j, n + 1):
                dp[i][j] = max(dp[i-1][j] if dp[i-1][j] >= stations[i-1][0] else 0, dp[i-1][j-1] + stations[i-1][1] if dp[i-1][j-1] >= stations[i-1][0] else 0)
            if dp[n][j] >= target:
                return j
        
        return -1

test = Solution()
stations = [[50,50]]
target = 100
startFuel = 50
print(test.minRefuelStops(target, startFuel, stations))