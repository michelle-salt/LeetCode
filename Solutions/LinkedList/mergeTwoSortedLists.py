# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            temp, origHead, otherHead, headToReturn = list1.next, list1, list2, list1
        else:
            temp, origHead, otherHead, headToReturn = list2.next, list2, list1, list2
            
        #check for case w/ one element (list1/2.next won't work)
        if not temp:
            headToReturn.next = otherHead
            return headToReturn
        
        while temp and origHead and otherHead:
            if temp.val <= otherHead.val:
                origHead.next = temp
                origHead = origHead.next
                if temp.next:
                    temp = temp.next
                else:
                    temp = None
                    origHead.next = otherHead
                    break
            else: 
                origHead.next = otherHead
                origHead = origHead.next
                if otherHead.next:
                    otherHead = otherHead.next
                else:
                    otherHead = None
                    origHead.next = temp
                    break
        
        return headToReturn
                
