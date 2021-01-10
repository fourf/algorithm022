class Solution:
    def jump(self, nums: List[int]) -> int:
        # BFS
        start, end, true_end = 0, 0, len(nums) - 1
        step = 0
        while end < true_end:
            step += 1
            start, end = end + 1, max(i + nums[i] for i in range(start, end + 1))
        return step

        # if len(nums) < 2:
        #     return 0
        # queue = deque([0])
        # step, position, end = 0, 0, len(nums) - 1
        # while queue:
        #     step += 1
        #     n = len(queue)
        #     for _ in range(n):
        #         i = queue.popleft()
        #         if i + nums[i] >= end:
        #             return step
        #         position = max(position, i + nums[i])

        #     queue.extend(range(i+1, position+1))

        # if len(nums) < 2:
        #     return 0
        # step, cur_end, farthest = 0, 0, 0
        # end = len(nums) - 1
        # for i in range(end):
        #     farthest = max(farthest, i + nums[i])
        #     if i == cur_end:
        #         step += 1
        #         cur_end = farthest
        #     if cur_end >= end:
        #         return step