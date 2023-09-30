class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for x in range(left, right+1):
            currNum = str(x)
            for num in currNum:
                if num == "0" or x % int(num) != 0:
                    currNum = 0
                    break
            if currNum:
                ans.append(x)

        return ans