class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [[False for _ in range(n + 1)] for _ in range(n)]
        dp[0][0] = True
        for i in range(1, n):
            for j in range(i):
                k = stones[i] - stones[j]
                if k <= i:
                    dp[i][k] = dp[j][k - 1] or dp[j][k] or dp[j][k + 1]
        return any(dp[-1])

        # dp = dict()
        # for stone in stones:
        #     dp[stone] = set()
        # dp[0].add(0)
        # for i, stone in enumerate(stones):
        #     for k in dp[stone]:
        #         for step in range(k - 1, k + 2):
        #             if step > 0 and stone + step in dp:
        #                 dp[stone + step].add(step)
        # return len(dp[stones[-1]]) != 0



        # def helper(j, k):
        #     if dp[j][k] > -1:
        #         return dp[j][k]
        #     if j == n - 1:
        #         return 1
        #     for i in range(j + 1, n):
        #         gap = stones[i] - stones[j]
        #         if k - 1 <= gap <= k + 1:
        #             if helper(i, gap) == 1:
        #                 dp[i][gap] = 1
        #                 return 1
        #             else:
        #                 dp[i][gap] = 0
        #     return 0

        # n = len(stones)
        # dp = [[-1 for _ in range(n)] for _ in range(n)]
        # return helper(0, 0) == 1
