class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = [0] * len(s)

        for x in range(len(s)):
            arr[indices[x]] = s[x]
        
        return "".join(arr)