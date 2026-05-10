class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        board = []
        def dfs(i, board):
            if i == n:
                res.append(board.copy())
                board = []
                return
            else:
                for j in range(n):
                    if self.isValid(j, n, board):
                        row = ('.' * j) + 'Q' + ('.' * (n-j-1))
                        board.append(row)
                        dfs(i + 1, board)
                        board.pop()
                return
        
        dfs(0, board)
        return res
    
    def isValid(self, j, n, board):
        rows = len(board)

        #row 2, col 1
        #right diagonal would be row 1 col 2, row 0 col 3
        #left diagonal would be row 1 col 0

        for i in range(rows):
            q_position = 0
            for char in board[i]:
                if char == 'Q':
                    break
                else:
                    q_position += 1
            
            #column
            if q_position == j:
                return False

            #diagonals to right
            if abs(i - rows) == abs(q_position - j):
                    return False

        return True
            

            
        


        