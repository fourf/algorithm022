class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 状态数组：dp[0,1][i] 包含nums[i]的子数组的最小，最大乘积
        # DP 方程 
        # dp = [[0] * len(nums) for _ in range(2)]
        # dp[0][0], dp[1][0] = nums[0], nums[0]
        # for i in range(1, len(nums)):
        #     dp[0][i] = min(dp[0][i - 1] * nums[i], dp[1][i - 1] * nums[i], nums[i])
        #     dp[1][i] = max(dp[0][i - 1] * nums[i], dp[1][i - 1] * nums[i], nums[i])
        # return max(dp[1])

        # 状态压缩
        maxp, minp, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            minp, maxp = min(minp * nums[i], maxp * nums[i], nums[i]), max(minp * nums[i], maxp * nums[i], nums[i])
            res = max(res, maxp)
        return res