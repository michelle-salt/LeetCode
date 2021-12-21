class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        [1, 3, 8, 0, 0, 8] [4, 5, 6] m=3 n=3
        
        counterM = m - 1
        counterN = n - 1
        for i = m+n to 0
            nums1[i] = max(nums1[m], nums2[i])
            counter -= 1 for whichever number was max
            if counterN == 0, break
        """
        
        counterM = m - 1
        counterN = n - 1

        if m == 0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
        elif n != 0:
            for i in range(m+n-1, -1, -1):
                maxNum = max(nums1[counterM], nums2[counterN])
                print(str(i) + "   :   " + str(nums1[i]))
                nums1[i] = maxNum
                print(str(i) + "   :   " + str(nums1[i]))
                if maxNum == nums1[counterM]:
                    counterM -= 1 
                else:
                    counterN -= 1
                if counterN == -1 or counterM == -1:
                    break
        if counterM == -1:
            for i in range(counterN + 1):
                nums1[i] = nums2[i]

        print(nums1)
        
        
