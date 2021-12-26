# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        allNodes = set()
        
        while head.next != None:
            if head in allNodes:
                return True
            allNodes.add(head)
            head = head.next
        
        return False
