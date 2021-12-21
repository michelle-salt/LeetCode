class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numWanted = 0
        for i in range(len(nums)):
            numWanted = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j]==numWanted:
                    return [i, j]
