class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Always adding 1 to the last term
        digits[-1] += 1
        
        # Loop through the list and if it is 10 it becomes 0 and carries on to the next
        # Time Complexity: O(digits), Space Complexity: O(1)
        carry_on = 0
        for i in range(len(digits)-1, -1, -1):
            if carry_on:
                digits[i] += 1
                carry_on = 0
            
            if digits[i]%10==0 and digits[i]!=0:
                digits[i] = 0
                carry_on = 1
        
        # If there is a carry on in the last iteration add the 1
        # If the first digit is equal to 1 then it was 10, hence append 0 
        if carry_on:
            digits[0] += 1
            if digits[0]==1:
                digits.append(0)
            
        return digits
            