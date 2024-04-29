# Best solution
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        temp = 0
        ans = -1

        for i in range(0,len(num)-1):
            if num[i] == num[i+1]:
                temp += 1
                if temp >= 2:
                    ans = max(ans, int(num[i]))
            else:
                temp = 0

        if ans != -1:
            return str(ans)*3
        return ""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        pointer = 0
        ans = -1

        while pointer < len(num)-2:
            if len(set(num[pointer:pointer+3]))==1:
                if int(num[pointer])>ans:
                    ans = int(num[pointer])
            pointer += 1
            
        if ans != -1:
            return str(ans)*3
        return ""