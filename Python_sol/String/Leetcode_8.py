# Time complexity O(n) Space Complexity O(1)
class Solution:
    def myAtoi(self, s: str) -> int:
        digits = "0123456789"
        signs = ["+", "-"]
        s = s.lstrip(" ")
        s1 = s.lstrip("0")
        nums = ""
        
        for i in s1:
            if i in signs:
                if not nums and s[0] == i:
                    nums += i
                else:
                    break
            
            elif i in digits:
                nums += i
            else:
                break
        
        try:
            nums = int(nums)
        except ValueError:
            return 0
        
        if nums < -2**31:
            nums = -2**31
        elif nums > 2**31 - 1:
            nums = 2**31 - 1
        return nums