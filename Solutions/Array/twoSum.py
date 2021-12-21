class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #7 - [2, 7, 3, 8, 19, 4]
        
        #for num in nums
            #if target - num is in dictionary (key)
            #return dictionary value (index) + current index
            #otherwise, add to dictionary (key --> num, value --> index)
            
        previousNums = {}
        indexCounter = 0
        for num in nums:
            if previousNums.get(target - num) != None:
                return [previousNums.get(target - num), indexCounter]
            previousNums.update({num : indexCounter})
            indexCounter += 1
