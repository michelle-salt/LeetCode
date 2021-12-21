class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #current sum = first num
        #for (start + 1.... end)
            #if current sum < 0
                #current sum  = max(current number, current sum)
            #else if current sum >= 0
                #current sum += current number
        #return current sum
        
        currentSum = maxVal = nums[0]
        for i in range(len(nums)):
            if (i != 0):
                if (currentSum < 0):
                    currentSum = max(nums[i], currentSum)
                else:
                    currentSum += nums[i]
                maxVal = max(currentSum, maxVal)
        return maxVal
                
