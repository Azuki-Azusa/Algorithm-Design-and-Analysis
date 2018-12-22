class Solution:
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if K == 0 or K + W <= N :
            return 1.0

        p = [0.0] * (N + 1)
        p[0] = 1.0

        num = 1.0

        for i in range(1, N + 1) :
            p[i] = num / W
            if i >= W :
                num -= p[i - W]
            if i < K :
                num += p[i]

        return sum(p[K:])

N = 21
K = 17
W = 10

test = Solution()
print(test.new21Game(N, K, W))

