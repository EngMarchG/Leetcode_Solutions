class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def final_answer(word):
            ans = []
            for letter in word:
                if letter == "#":
                    if ans:
                        ans.pop()
                else:
                    ans.append(letter)
            return ans
        ans1 = final_answer(s)
        ans2 = final_answer(t)
        return ans1 == ans2