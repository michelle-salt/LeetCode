# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         if empty, return list
        
#         Two cases: head must be removed (or not)
#             case 1 (head removed):
                
#         newHead = head
        
#         loop through each element
#             if newHead.val == val:
#                 newHead = head.next
#             elif head.val == val:
#                 head.next = head.next.next
                
#             head = head.next if possible
        
#         return newHead
                
        if not head:
            return head
        
        if not head.next:
            if head.val == val:
                return None
            return head
        
        pointer = head
        
        while pointer.next:
            if head.val == val:
                if pointer != head:
                    pointer = pointer.next
                head = head.next
            elif pointer.next.val == val:
                if pointer.next.next:
                    pointer.next = pointer.next.next
                else:
                    pointer.next = None
                    break
            else:
                pointer = pointer.next
            
        return head
                
