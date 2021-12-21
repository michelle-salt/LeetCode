class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        counterM = m - 1
        counterN = n - 1
        counterTotal = m + n - 1
        
        for index in range(counterTotal, -1, -1):
            if counterN == -1:
                nums1[index] = nums1[counterM]
                counterM -= 1
            elif counterM == -1:
                nums1[index] = nums2[counterN]
                counterN -= 1
            else:
                nums1[index] = max(nums1[counterM], nums2[counterN])
                if max(nums1[counterM], nums2[counterN]) == nums1[counterM]:
                    counterM -= 1
                else:
                    counterN -= 1
