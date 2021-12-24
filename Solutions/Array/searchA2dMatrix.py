class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        botRow = 0
        topRow = len(matrix)
        midRow = (topRow - botRow)// 2 + botRow
        
        n = len(matrix[0])-1
        botCol = 0
        topCol = n + 1
        midCol = (topCol - botCol)// 2 + botCol
        
        for row in range(len(matrix)):
            if target >= matrix[midRow][0] and target <= matrix[midRow][n]:
                for col in range(n+1):
                    if target == matrix[midRow][midCol] or target == matrix[midRow][0]:
                        return True
                    elif target < matrix[midRow][midCol]:
                        topCol = midCol + 1
                        midCol = (topCol - botCol)// 2 + botCol
                    elif target > matrix[midRow][midCol]:
                        botCol = midCol
                        midCol = (topCol - botCol)// 2 + botCol
                    else:
                        return False
            elif target < matrix[midRow][0]:
                if midRow == 1:
                    midRow = 0
                else:
                    topRow = midRow + 1
                    midRow = (topRow - botRow)// 2 + botRow
            elif target > matrix[midRow][n]:
                botRow = midRow
                midRow = (topRow - botRow)// 2 + botRow
            else:
                return False

        return False
            
