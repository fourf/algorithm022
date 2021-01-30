class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(x, y, node):
            c = board[x][y]
            w = node[c].pop('#', False)
            if w:
                res.append(w)
            if not node[c]:
                node.pop(c)
                return
            board[x][y] = '#'
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and board[i][j] in node[c]:
                    dfs(i, j, node[c])
            board[x][y] = c
        m, n = len(board), len(board[0])
        root = dict()
        for w in words:
            node = root
            for c in w:
                node = node.setdefault(c, {})
            node['#'] = w 
        res = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(i, j, root)
        return res