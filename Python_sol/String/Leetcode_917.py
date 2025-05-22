class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s)-1
        temp = [0] * len(s)

        while left <= right:
            while not s[left].isalpha() and left < right:
                temp[left] = s[left]
                left += 1
            while not s[right].isalpha() and right > left:
                temp[right] = s[right]
                right -= 1
            temp[right] = s[left]
            temp[left] = s[right]
            left += 1
            right -= 1
        return "".join(temp)
