class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
# [1, 2, 2, 3, 4] [2, 4, 4, 6, 8]

# resultCounter, dictionary (key = num, value = times appears in nums1)
# for num in nums1
#     if key in dictionary, value += 1
#     else, put key in dictionary, value = 1
    
# for num in nums2
#     if num in dictionary (as key) and value > 0
#         add num to result array
#         value -= 1
#         counterResult += 1
        
# return result

        dictionary = {}
        result = []
        
        for num in nums1:
            if dictionary.get(num) != None:
                dictionary[num] += 1
            else:
                dictionary.update({num:1})
        
        for num in nums2:
            if dictionary.get(num) != None and dictionary.get(num) > 0:
                result.append(num)
                dictionary[num] -= 1
                
        return result
