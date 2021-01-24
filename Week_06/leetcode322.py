class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP
        # dp = [0] + [amount + 1] * amount
        # for i in range(1, amount + 1):
        #     for coin in coins:
        #         if i - coin >= 0:
        #             dp[i] = min(dp[i], dp[i - coin] + 1)
        # return dp[amount] if dp[amount] != amount + 1 else -1

        # dfs
        def dfs(amount, i, count):
            if amount == 0:
                self.res = min(self.res, count)
                return 1
            if i == len(coins):
                return
            k = amount // coins[i]
            if count + k >= self.res:
                return
            while k >= 0:
                if dfs(amount - k * coins[i], i + 1, count + k):
                    return 
                k -= 1
        self.res = amount + 1
        coins.sort(reverse=True)
        dfs(amount, 0, 0)
        return self.res if self.res != amount + 1 else -1