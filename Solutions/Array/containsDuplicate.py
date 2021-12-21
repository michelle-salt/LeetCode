class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # //for each element in array
        #     //if num is in dictionary, return false
        #     //otherwise, add it to dictionary
            
        all_nums = {}
        for num in nums:
            if (all_nums.get(num) != None):
                return True;
            else:
                all_nums.update({num: 1});
        return False;
