class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m= len(matrix)
        n = len(matrix[0])
        top = len(matrix) -1 
        bottom = 0
        row = 0
        #Target in matrix
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        # binary search in rows
        while bottom <= top:
            mid = (bottom + top) // 2
            
            # If target is smaller than the start of this row, go up
            if target < matrix[mid][0]:
                top = mid - 1
            # If target could be in this row or a later row, go down
            else:
                row = mid         # Mark this as a candidate row!
                bottom = mid + 1  # Keep searching down to find the closest row
                
                

        return target in matrix[row]
