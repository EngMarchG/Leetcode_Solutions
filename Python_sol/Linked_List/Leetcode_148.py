# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head
        
        # Time complexity O(3N) = O(N) Space complexity O(N)
        while temp:
            arr.append(temp.val)
            temp = temp.next
            
        arr.sort()
        temp = head
        
        for x in arr:
            temp.val = x
            temp = temp.next
        return head