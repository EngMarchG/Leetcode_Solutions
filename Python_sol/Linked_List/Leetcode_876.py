
# Middle of the Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        counter = 0
        
        # Cheating method, otherwise time complexity O(N+N/2) = O(N)
        # Time complexity O(N) Space complexity O(1)
        while temp:
            temp = temp.next
            counter += 1
        counter = int(counter/2)
        nxt = ".next"*counter
        head = eval("head" + nxt)
        return head

"""Normal Method
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        counter = 0
        while temp:
            temp = temp.next
            counter += 1
        counter = int(counter/2)
        
        for x in range(counter):
            head = head.next
        return head
"""