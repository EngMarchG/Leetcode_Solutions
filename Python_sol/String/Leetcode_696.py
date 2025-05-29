class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        left, right = 0, 1
        count, prev_count, curr_count = 0, 0, 1

        while right < len(s):
            if s[right] == s[right - 1]:
                curr_count += 1
            else:
                count += min(prev_count, curr_count)
                prev_count, curr_count = curr_count, 1
            right += 1
        count += min(prev_count, curr_count)
        return count