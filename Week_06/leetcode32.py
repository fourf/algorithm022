class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # n = len(s)
        # dp = [0] * n
        # res = 0
        # for i in range(1, len(s)):
        #     if s[i] == ')':
        #         if s[i - 1] == '(':
        #             dp[i] = dp[i - 2] + 2
        #         elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
        #             dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
        #         res = max(res, dp[i])
        # return res

        # stack, res = [-1], 0
        # for i, c in enumerate(s):
        #     if c == '(':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if not stack:
        #             stack.append(i)
        #         else:
        #             res = max(res, i - stack[-1])
        # return res

        res = 0
        left, right = 0, 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
                if right > left:
                    left, right = 0, 0
                elif right == left:
                    res = max(res, right * 2)
        left, right = 0, 0
        for c in s[::-1]:
            if c == ')':
                right += 1
            else:
                left += 1
                if left > right:
                    left, right = 0, 0
                elif left == right:
                    res = max(res, left * 2)
        return res