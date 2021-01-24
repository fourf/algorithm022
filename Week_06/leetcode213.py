class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(start, end):
            a, b = 0, 0
            for i in range(start, end):
                a, b = b, max(b, a + nums[i])
            return b
        return max(helper(0, len(nums) - 1), helper(1, len(nums))) if len(nums) > 1 else nums[0]