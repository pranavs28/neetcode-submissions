class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        freq_row = [set() for _ in range(9)]
        freq_col = [set() for _ in range(9)]
        freq_box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                #row eval
                if board[i][j] in freq_row[i]:
                    return False
                else:
                    freq_row[i].add(board[i][j])

                #col eval
                if board[i][j] in freq_col[j]:
                    return False
                else:
                    freq_col[j].add(board[i][j])

                #box eval
                box = (i // 3) * 3 + (j//3)
                if board[i][j] in freq_box[box]:
                    return False
                else:
                    freq_box[box].add(board[i][j])

        return True





        #validate boxes
        
        