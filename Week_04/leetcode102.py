# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS
        # queue = deque([root])
        # res = []
        # while queue:
        #     n = len(queue)
        #     tmp = []
        #     for _ in range(n):
        #         root = queue.popleft()
        #         if root:
        #             tmp.append(root.val)
        #             queue.append(root.left)
        #             queue.append(root.right)
        #     if tmp:
        #         res.append(tmp)
        # return res

        # DFS
        def dfs(level, root):
            if not root:
                return
            if level == len(res):
                res.append([])
            res[level].append(root.val)
            dfs(level+1, root.left)
            dfs(level+1, root.right)
        res = []
        dfs(0, root)
        return res