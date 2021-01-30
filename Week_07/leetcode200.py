class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # def dfs(i, j):
        #     grid[i][j] = '0'
        #     for k in range(4):
        #         x, y = i + dx[k], j + dy[k]
        #         if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
        #             dfs(x, y)


        # dx = [-1, 0, 1, 0]
        # dy = [0, 1, 0, -1]
        # m, n = len(grid), len(grid[0])
        # res = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == '1':
        #             res += 1
        #             dfs(i, j)
        # return res

        m, n = len(grid), len(grid[0])
        p = defaultdict(int)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    p[i * n + j] = i * n + j
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for dx, dy in ((0, 1), (1, 0)):
                        x, y = i + dx, j + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                            self.union(p, i * n + j, x * n + y)
        res = len(set(self.find(p, i) for i in p))
        return res

    def union(self, p, i, j):
        p1 = self.find(p, i)
        p2 = self.find(p, j)
        p[p2] = p1

    def find(self, p, i):
        root = i 
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            p[i], i = root, p[i]
        return root