class Solution:
    def minLength(self, s: str) -> int:
        s = [letter for letter in s]
        i = 0
        remove_list = ["AB", "CD"]

        while i < len(s) - 1:
            if s[i] + s[i+1] in remove_list:
                s.pop(i)
                s.pop(i)
                if i > 0:
                    i -= 1
            else:
                i += 1
        
        return len(s)
