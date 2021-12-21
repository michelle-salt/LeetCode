class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSums = []
        i = 0
        for num in nums:
            if i == 0:
                runningSums.append(nums[i])
            else: 
                runningSums.append(nums[i] + runningSums[i-1])
            i += 1
        return runningSums
