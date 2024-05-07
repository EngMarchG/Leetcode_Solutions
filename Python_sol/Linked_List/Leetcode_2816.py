# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        num = []
        sys.set_int_max_str_digits(10001)
        
        while temp:
            num.append(str(temp.val))
            temp = temp.next
        num = int("".join(num))*2
        num = str(num)


        temp = head
        for i, number in enumerate(num):
            if i < len(num)-1 and temp.next is None:
                temp.next = ListNode(0)    
            temp.val = int(number)
            temp = temp.next
        
        return head