class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        temp = [0, 0]

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                if i+1 != len(s)-1:
                    continue
                elif i+2 - temp[0] > 2:
                    temp[1] = i + 1
                    ans.append(temp)
            else:
                if i+1 - temp[0] > 2:
                    temp[1] = i
                    ans.append(temp)
                temp = [i+1, i+1]
        return ans 