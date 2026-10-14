class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        right = len(matrix)-1
        rowIdx = None
        while right>= left:
            mid = left + (right - left)//2
            if target>= matrix[mid][0] and target<=matrix[mid][-1]:
                rowIdx = mid
                break
            if target > matrix[mid][-1]:
                left = mid+1
            else:
                right = mid-1

        if rowIdx is None:
            return False    
        
        left, right = 0, len(matrix[rowIdx]) -1

        while right>=left:
            mid = left + (right-left)//2
            if matrix[rowIdx][mid] == target:
                return True
            
            if target > matrix[rowIdx][mid]:
                left = mid+1
            else:
                right = mid-1
        
        return False