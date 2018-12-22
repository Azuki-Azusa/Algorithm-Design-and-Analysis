class Solution:
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 3
        if n == 2:
            return 8
        mod = 1000000007
        A = [0] * n
        P = [0] * n
        L = [0] * n
        A[0] = 1
        A[1] = 2
        A[2] = 4
        L[0] = 1
        L[1] = 3
        P[0] = 1

        for i in range(1, n):
            A[i - 1] %= m
            P[i - 1] %= m
            L[i - 1] %= m

            if i > 2:
                A[i] = ((A[i-1] + A[i-2]) % mod + A[i-3]) % mod
            P[i] = ((A[i-1] + P[i-1]) % mod + L[i-1]) % mod
            if i > 1:
                L[i] = ((A[i-1] + P[i-1]) % mod + (A[i-2] + P[i-2]) % mod) % mod
        return ((A[n-1] + P[n-1]) % mod + L[n-1] % mod) % mod

test = Solution()
print(test.checkRecord(4))