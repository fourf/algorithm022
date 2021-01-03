class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 库函数
        # return list(combinations(range(1, n+1), k))
        
        def dfs(num):
            if len(com) == k:
                res.append(com[:])
                return 
            for j in range(num, n+1):
                com.append(j)
                dfs(j+1)
                com.pop()
        res, com = [], []
        dfs(1)
        return res