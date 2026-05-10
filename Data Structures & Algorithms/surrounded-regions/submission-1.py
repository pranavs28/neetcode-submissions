class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])
        def dfs(r,c):
            if min(r,c) < 0 or r == rows or c == cols or board[r][c] == 'X' or board[r][c] == '#':
                return
            
            board[r][c] = '#'

            neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in neighbors:
                dfs(r + dr, c + dc)
            return
        
        for r in range(rows):
            if board[r][0] != 'X' and board[r][0] != '#':
                dfs(r,0)
            if board[r][cols - 1] != 'X' and board[r][cols - 1] != '#':
                dfs(r, cols - 1)
        
        for c in range(cols):
            if board[0][c] != 'X' and board[0][c] != '#':
                dfs(0,c)
            if board[rows - 1][c] != 'X' and board[rows - 1][c] != '#':
                dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '#':
                    board[r][c] = 'O'
        
        return
        