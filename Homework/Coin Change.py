class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        array = [amount + 1] * (amount + 1)
        array[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if (coin <= i):
                    array[i] = min(array[i], array[i - coin] + 1)
        
        if array[amount] != amount + 1:
            return array[amount]
        else:
            return -1

coins = [1, 2, 5]
amount = 11
test = Solution()
print(test.coinChange(coins, amount))