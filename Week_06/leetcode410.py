class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 二分
        # left, right = max(nums), sum(nums)
        # while left < right:
        #     mid = (left + right) // 2
        #     count, tmp = 0, 0
        #     for i in nums:
        #         tmp += i 
        #         if tmp > mid:
        #             tmp = i 
        #             count += 1
        #     count += 1
        #     if count > m:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return left

        # dp[i][j] 前 i 个数分成 j 段的最大值的最小
        n = len(nums)
        dp = [[math.inf for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = 0
        sub = [0]
        for i in nums:
            sub.append(sub[-1] + i)
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sub[i] - sub[k]))
        return dp[n][m]