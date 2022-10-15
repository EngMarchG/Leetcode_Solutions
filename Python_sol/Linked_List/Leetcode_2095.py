# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If only 1 element exists
        if not head.next:
            head = None
            return head
        
        counter = 1
        count_slow = 0
        
        slow = head
        fast = head.next
        
        # Time complexity O(N) Space complexity O(1)
        while fast:
            if not counter % 2:
                slow = slow.next
                count_slow += 1
            fast = fast.next
            counter += 1
        
        # Avoiding none types with 2 elements
        if counter == 2:
            head.next = None
            return head
        # If it is even then the slow count has to be adjusted
        if not counter//2 == count_slow:
            slow = slow.next
        slow.val = slow.next.val
        slow.next = slow.next.next

        return head
        