# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        arr = []
        i = 1
        curr_max = 0

        while temp:
            if temp.val > curr_max:
                arr = []
                curr_max = temp.val

            arr.append((temp.val, i))
            i += 1
            temp = temp.next

        arr.sort(key=lambda x: (-x[0], x[1]))
        
        dummy = ListNode(1)
        temp = dummy
        temp.next = head
        
        pointer = 0
        relative_pointer = 0
        while temp.next and pointer < len(arr):
            if temp.next.val == arr[pointer][0]:
                while pointer < len(arr) and arr[pointer][1] <= arr[relative_pointer][1]:
                    pointer += 1
                relative_pointer = pointer
                temp = temp.next
            else:
                temp.next = temp.next.next

        return dummy.next