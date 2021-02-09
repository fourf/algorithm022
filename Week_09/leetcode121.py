class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # cost, pro = math.inf, 0
        # for v in prices:
        #     cost = min(cost, v)
        #     pro = max(pro, v - cost)
        # return pro

        # dp[k][0, 1] -> 第k次交易0（不持有），1（持有）的状态
        # dp = [[0, 0], [0, -math.inf]]
        # for v in prices:
        #     dp[1][0] = max(dp[1][0], dp[1][1] + v)
        #     dp[1][1] = max(dp[1][1], dp[0][0] - v)
        # return dp[1][0]

        # dp = [0, -math.inf]
        # for v in prices:
        #     dp[0] = max(dp[0], dp[1] + v)
        #     dp[1] = max(dp[1], -v)
        # return dp[0]

        # 第i天卖出股票的最大利润
        dp, res = 0, 0
        for i in range(1, len(prices)):
            dp = max(dp, 0) + prices[i] - prices[i - 1]
            res = max(res, dp)
        return res