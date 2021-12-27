# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if list is 0 or 1 values long:
#             return list
        
#         temp = ListNode()
#         temp.val = head.val
#         temp.next = None
        
#         loop through head.next until end of list
#             temp2 = ListNode()
#             temp2.val = currentLocation.val
#             temp2.next = temp
#             temp = temp2
        
#         return temp

        if not head or not head.next:
            return head
        
        newListPointer = ListNode()
        newListPointer.val = head.val
        newListPointer.next = None
        
        head = head.next
        
        while head:
            newVal = ListNode()
            newVal.val = head.val
            newVal.next = newListPointer
            
            newListPointer = newVal
            head = head.next
        
        return newListPointer
            
            
