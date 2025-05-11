class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = []
        for letter in s:
            cur_ord = ord(letter)
            if cur_ord > 64 and cur_ord < 91:
                ans.append(chr(cur_ord+32))
            else:
                ans.append(letter)
        return ''.join(ans)
