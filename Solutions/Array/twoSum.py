class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numWanted = 0
        length = len(nums)
        for i in range(length):
            numWanted = target - nums[i]
            for j in range(i+1, length):
                if nums[j]==numWanted:
                    return [i, j]
