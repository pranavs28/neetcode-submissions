class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = {}
        row_len = len(board)
        col_len = len(board[0])

        def exist_helper(board, word, i, r, c):
            if r < 0 or r >= row_len or c < 0 or c >= col_len or board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            
            visited[(r,c)] = True
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited:
                    if exist_helper(board, word, i + 1, nr, nc):
                        return True
            
            visited.pop((r,c))
            return False
    
        for i in range(row_len):
            for j in range(col_len):
                if exist_helper(board, word, 0, i, j):
                    return True
        return False