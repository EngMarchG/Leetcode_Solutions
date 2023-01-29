# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Time complexity O(2N) Space complexity O(N)
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        fi = 0
        end = len(arr)-1
        while fi < end:
            if arr[fi] != arr[end]:
                return False
            fi += 1
            end -= 1
        return True