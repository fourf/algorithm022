class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 状态数组 dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        m, n = len(grid), len(grid[0])
        dp = [0] + [math.inf] * n
        for i in range(m):
            for j in range(n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-2]