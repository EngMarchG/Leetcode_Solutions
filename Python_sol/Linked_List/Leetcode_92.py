# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pos = 1
        arr = []

        head1 = head2 = head
        while head1:
            if pos > right:
                break
            elif pos >= left:
                arr.append(head1.val)
            pos +=1
            head1 = head1.next
        
        pos = 1
        while head2:
            if pos > right:
                break
            elif pos >= left:
                head2.val = arr[-1]
                arr.pop()
            pos += 1
            head2 = head2.next
        
        return head
                   