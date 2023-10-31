class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
    

# Worse Solution:
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        setto = set(s)
        if set(s[0]) == setto and len(s)>1:
            return True
        elif len(s) == 2:
            return s[0]==s[1]
        
        for i in range(1, len(s)//2+1):
            if len(s) % (i+1) == 0 and set(s[:i+1]) == setto:
                flag = True
                temp = 1
                while (i+1) * temp < len(s):
                    if s[(i+1)*temp:(i+1)*temp+i+1] != s[:i+1]:
                        flag = False
                        break
                    temp += 1
                if flag:
                    return True
