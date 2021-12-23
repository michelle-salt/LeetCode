class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #initialize empty colDict, rowDict, squareDict
        #squareNum = 0
        #square = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        
        #for each row
            #for each col
                #if not in colDict --> if access val == current col #
                    #add to colDict, key = #, val = col #
                #else
                    #return false
                
                #if not in rowDict --> if access val == current row #
                    #add to rowDict, key = #, val = row #
                #else
                    #return false
                    
                #if col == 3
                    #square # += 1
                #elif col ==6
                    #square # += 1
                #elif col == 0
                    #square # += 1
                    
                    
                #if not in squareDict --> if access val == current square #
                    #add to squareDict, key = #, val = square #
                #else
                    #return false
            
            #if row == 3
                #square # = 3
            #elif row ==6
                #square # = 6
            #elif row == 0
                #square # = 0
        
        #return true
                
        colDict = {}
        rowDict = {}
        squareDict = {}
        
        squareNum = 0
        
        for r in range(len(board)):
            rowDict = {}
            
            if r < 3:
                squareNum = 0
            elif r < 6:
                squareNum = 3
            else:
                squareNum = 6 
            for c in range(len(board[0])):
                if c == 0 or c == 3 or c == 6:
                    squareNum += 1
                        
                if (board[r][c] != "."):
                    if rowDict.get(board[r][c]) == None:
                        rowDict.update({board[r][c] : r})
                    else:
                        return False

                    if colDict.get(board[r][c]) != None:
                        if c in colDict.get(board[r][c]):
                            return False
                        else:
                            colDict.get(board[r][c]).add(c)
                    else:
                        colDict.update({board[r][c] : {c}}) 

                    if squareDict.get(board[r][c]) != None:
                        if squareNum in squareDict.get(board[r][c]):
                            return False
                        else:
                            squareDict.get(board[r][c]).add(squareNum)
                    else:
                        squareDict.update({board[r][c] : {squareNum}}) 
                    
        return True
