class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分
        # left, right = 0, x
        # res = 0
        # while left <= right:
        #     mid = (left + right) // 2
        #     if mid * mid <= x:
        #         res = mid
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return res

        # 牛顿
        # r = x
        # while r * r > x:
        #     r = (r + x // r) // 2
        # return r

        r = x
        while r * r - x > 1e-6:
            r = (r + x / r) / 2
        return int(r)