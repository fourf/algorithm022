class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[i][j] (i, j)间是否是回文串 i <= j
        # n = len(s)
        # dp = [[0 for _ in range(n)] for _ in range(n)]
        # count = 0
        # for j in range(n):
        #     for i in range(j + 1):
        #         if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
        #             dp[i][j] = True
        #             count += 1
        # return count

        n = len(s)
        dp = [False for _ in range(n)]
        count = 0
        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1]):
                    dp[i] = True
                    count += 1
                else:
                    dp[i] = False
        return count