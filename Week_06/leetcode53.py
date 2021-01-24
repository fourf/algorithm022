class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [0 for _ in range(n)]
        # dp[0], res = nums[0], nums[0]
        # for i in range(1, n):
        #     dp[i] = max(dp[i - 1], 0) + nums[i]
        #     res = max(dp[i], res)
        # return res

        pre = res = nums[0]
        for i in range(1, len(nums)):
            pre = max(pre, 0) + nums[i]
            res = max(pre, res)
        return res