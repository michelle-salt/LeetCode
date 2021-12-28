# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if len(list) == 0 or == 1:
#             return head
        
#         prev, curr = head, head.next
#         loop through all elements, starting at second (curr):
#             if curr.val == prev.val:
#                 prev.next = curr.next
#                 curr = prev.next
#             else:
#                 curr = curr.next
#                 prev = prev.next
#         return head

        if not head: # or not head.next:
            return head
        
        prev, curr = head, head.next
        
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
                curr = prev.next
            else:
                curr = curr.next
                prev = prev.next
        return head
