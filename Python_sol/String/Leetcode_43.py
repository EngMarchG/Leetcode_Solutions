class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Time complexity O(num1+num2) Space complexity O(1)
        return str(int(num1)*int(num2))



"""Less efficient method
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # Time Comp: O(2(num1+num2)), Space Comp: O(num1+num2)
        hmap1 = {num1: [i for i in num1]}
        hmap2 = {num2: [i for i in num2]}
        
        return str(int("".join(hmap1[num1]))*int("".join(hmap2[num2])))
"""