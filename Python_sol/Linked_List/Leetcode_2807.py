# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def gcd(a, b):
            if(b == 0):
                return a
            else:
                return gcd(b, a % b)

        p1 = p2 = head
        p2 = head.next
        while p2:
            val = gcd(p1.val, p2.val)
            if val:
                p1.next = ListNode(val, p2)
            p1 = p2
            p2 = p2.next
        
        return head