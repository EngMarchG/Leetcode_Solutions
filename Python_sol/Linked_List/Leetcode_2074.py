class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        array = []

        counts = 0
        temp = 0
        right_bound = ((temp + 1)*(temp+2))//2
        temp_arr = []
        while curr:
            if counts >= right_bound:
                array.append(temp_arr)
                temp_arr = []
                temp += 1
                right_bound = ((temp + 1)*(temp+2))//2
            temp_arr.append(curr.val)
            curr = curr.next
            counts += 1
        array.append(temp_arr)
        
        head = ListNode(0)
        temp = head

        for i, arr in enumerate(array):
            if (not (i+1)%2 and not len(arr)%2) or (i==len(array)-1 and not len(arr)%2):
                arr = arr[::-1]
            for ele in arr:
                temp.next = ListNode(ele)
                temp = temp.next

        head = head.next
        return head