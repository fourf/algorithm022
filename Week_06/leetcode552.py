class Solution:
    def checkRecord(self, n: int) -> int:
        # O(3^n)
        # @lru_cache
        # def dfs(level, hasA, L1, L2):
        #     if level == n:
        #         return 1
        #     p, a, l = 0, 0, 0
        #     p = dfs(level + 1, hasA, False, False)  # P
        #     if not hasA:
        #         a = dfs(level + 1, True, False, False) # A
        #     if not (L1 and L2):
        #         l = dfs(level + 1, hasA, L2, True)  # L
        #     return (p + a + l) % (10 ** 9 + 7)
        # return dfs(0, False, False, False)

        # dp
        # _mod = 10 ** 9 + 7
        # dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        # dp[0][0][0], dp[0][0][1], dp[0][1][0] = 1, 1, 1
        # for i in range(1, n):
        #     # p
        #     dp[i][0][0] = (dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]) % _mod
        #     dp[i][1][0] = (dp[i-1][1][0] + dp[i-1][1][1] + dp[i-1][1][2]) % _mod

        #     # l
        #     dp[i][0][1] = dp[i-1][0][0]
        #     dp[i][0][2] = dp[i-1][0][1]
        #     dp[i][1][1] = dp[i-1][1][0]
        #     dp[i][1][2] = dp[i-1][1][1]

        #     # a
        #     dp[i][1][0] += (dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]) % _mod
        # return (sum(dp[-1][0]) + sum(dp[-1][1])) % _mod

        _mod = 10 ** 9 + 7
        dp = [[0 for _ in range(3)] for _ in range(2)]
        dp[0][0], dp[0][1], dp[1][0] = 1, 1, 1
        for i in range(1, n):
            t00, t10 = dp[0][0], dp[1][0]
            dp[1][0] = (sum(dp[0]) + sum(dp[1])) % _mod
            dp[0][0] = (t00 + dp[0][1] + dp[0][2]) % _mod
            dp[0][1], dp[0][2] = t00, dp[0][1]
            dp[1][1], dp[1][2] = t10, dp[1][1]
        return (sum(dp[0]) + sum(dp[1])) % _mod