class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for m in range(2, n):
            for i in range(n - m):
                j = i + m 
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        return dp[0][-1]