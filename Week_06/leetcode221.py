class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 求最大面积，找最大边长
        # 状态数组 dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        # 以(i, j)为右下角的正方形的边长
        # m, n = len(matrix), len(matrix[0])
        # dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # res = 0
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == '1':
        #             dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
        #             res = max(res, dp[i + 1][j + 1])
        # return res * res

        # 状态压缩
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)
        res = 0
        for i in range(m):
            pre = 0
            for j in range(n):
                tmp = dp[j]
                dp[j] = min(pre, dp[j], dp[j - 1]) + 1 if matrix[i][j] == '1' else 0
                pre = tmp
                res = max(res, dp[j])
        return res * res