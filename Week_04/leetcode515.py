# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # BFS
        # if not root:
        #     return []
        # queue, res = deque([root]), []
        # while queue:
        #     num = -math.inf
        #     n = len(queue)
        #     for _ in range(n):
        #         node = queue.popleft()
        #         num = max(num, node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     res.append(num)
        # return res
        queue, res = [root], []
        while any(queue):
            res.append(max(node.val for node in queue))
            queue = [kid for node in queue for kid in (node.left, node.right) if kid]
        return res

        # DFS
        # def dfs(level, root):
        #     if not root:
        #         return
        #     if level == len(res):
        #         res.append(root.val)
        #     else:
        #         res[level] = max(res[level], root.val)
        #     dfs(level+1, root.left)
        #     dfs(level+1, root.right)
        # res = []
        # dfs(0, root)
        # return res