class Solution:
    def generate(self, numRows: int) -> List[List[int]]:        
        #first row = [1]
        #for i in range(1, numRows)
            #element 0 = 1
            #element n = previousRow[n-1]+previousRow[n]
            #last element (i) = 1
                #append row to 2D list
                #set element to 0
                #set newRow = []
        #return result
        
        result = []
        result.append([1])
        newRow = []
        element = 0
        
        for i in range(2, numRows+1):
            for j in range(i):
                if element == 0:
                    newRow.append(1)
                elif element == i-1:
                    newRow.append(1)
                    break
                else:
                    newRow.append(result[i-2][element-1]+result[i-2][element])
                element += 1
            result.append(newRow)
            element = 0
            newRow = []
            
        return result
