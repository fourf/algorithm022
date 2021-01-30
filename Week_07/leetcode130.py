class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # BFS
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1 and board[i][j] == 'O':
                    q.append((i, j))
                    while q:
                        x, y  = q.popleft()
                        if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                            board[x][y] = '#'
                            q.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'


        # def dfs(x, y):
        #     board[x][y] = '#'
        #     for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        #         i, j = x + dx, y + dy
        #         if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
        #             dfs(i, j)
        # if not board or not board[0]:
        #     return
        # m, n = len(board), len(board[0])
        # for i in range(m):
        #     if board[i][0] == 'O':
        #         dfs(i, 0)
        #     if board[i][n - 1] == 'O':
        #         dfs(i, n - 1)
        # for i in range(n):
        #     if board[0][i] == 'O':
        #         dfs(0, i)
        #     if board[m - 1][i] == 'O':
        #         dfs(m - 1, i)
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == 'O':
        #             board[i][j] = 'X'
        #         elif board[i][j] == '#':
        #             board[i][j] = 'O'

        # UnionFindSet
        # if not board or not board[0]:
        #     return
        # m, n = len(board), len(board[0])
        # p, dummy = UnionFindSet(m * n + 1), m * n 
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == 'O':
        #             if i == 0 or i == m - 1 or j == 0 or j == n - 1:
        #                 p.union(i * n + j, dummy)
        #             else:
        #                 for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        #                     x, y = i + dx, j + dy
        #                     if board[x][y] == 'O':
        #                         p.union(i * n + j, x * n + y)
        # for i in range(m):
        #     for j in range(n):
        #         if p.find(i * n + j) != p.find(dummy):
        #             board[i][j] = 'X'
    
class UnionFindSet:
    def __init__(self, n):
        self.p = [i for i in range(n)]

    def union(self, i, j):
        self.p[self.find(j)] = self.find(i)

    def find(self, i):
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]