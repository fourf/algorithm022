class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # UnionFindSet
        n = len(isConnected)
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(i):
                if isConnected[i][j] == 1:
                    self.union(p, i, j)
        return len(set(self.find(p, i) for i in range(n)))

        # DFS
        # def dfs(i):
        #     visited.add(i)
        #     for j in range(n):
        #         if isConnected[i][j] and j not in visited:
        #             dfs(j)
        # n = len(isConnected)
        # visited = set()
        # count = 0
        # for i in range(n):
        #     if i not in visited:
        #         dfs(i)
        #         count += 1
        # return count

        # BFS
        # n = len(isConnected)
        # visited = set()
        # count = 0
        # for i in range(n):
        #     if i not in visited:
        #         count += 1
        #         q = deque([i])
        #         while q:
        #             k = q.popleft()
        #             visited.add(k)
        #             for j in range(n):
        #                 if isConnected[k][j] and j not in visited:
        #                     q.append(j)
        # return count
                    

    def union(self, p, i, j):
        p1 = self.find(p, i)
        p2 = self.find(p, j)
        p[p2] = p1

    def find(self, p, i):
        if p[i] != i:
            p[i] = self.find(p, p[i])
        return p[i]