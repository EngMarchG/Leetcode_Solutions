# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 1
        temp = head
        while temp:
            temp = temp.next
            counter += 1
        
        
        temp = head
        prev = temp
        for pos in range(1, counter):
            if pos == counter - n:
                if temp == prev:
                    head = head.next
                    break
                
                temp = temp.next
                prev.next = temp
                break
            prev = temp
            temp = temp.next
        return head