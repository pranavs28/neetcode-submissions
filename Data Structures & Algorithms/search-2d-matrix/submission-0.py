class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low_row = 0
        high_row = len(matrix) - 1

        row_len = len(matrix[0])
        row = -1
        while low_row <= high_row:
            mid = (high_row + low_row) // 2

            if target < matrix[mid][0]:
                high_row = mid - 1
            elif target > matrix[mid][row_len - 1]:
                low_row = mid + 1
            else:
                row = mid
                break
        
        if row == -1:
            return False
        
        low = 0
        high = row_len - 1
        while low <= high:
            mid = (high + low) // 2

            if target < matrix[row][mid]:
                high = mid - 1
            elif target > matrix[row][mid]:
                low = mid + 1
            else:
                return True
        
        return False


    