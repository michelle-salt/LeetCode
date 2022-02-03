# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         create arrayList var to store node values
#         loop through all nodes:
#             put node.val in index i of arrayList
            
#         loop through elements in arrayList / 2:
#                 if !(arrayList[i] == arrayList[length - 1]):
#                     return false
                
#         return true

        vals = []
        node = head
        
        while node:
            vals.append(node.val)
            node = node.next
            
        length = len(vals) - 1
        
        for i in range(floor(len(vals)/2)):
            if vals[i] != vals[length - i]:
                return False
        
        return True
