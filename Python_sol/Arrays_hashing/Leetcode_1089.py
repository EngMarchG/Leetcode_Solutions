class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        pos = 0
        origin = len(arr)
        while pos < origin:
            if arr[pos] == 0:
                arr.insert(pos, 0)
                arr.pop()
                pos += 1

            pos += 1s