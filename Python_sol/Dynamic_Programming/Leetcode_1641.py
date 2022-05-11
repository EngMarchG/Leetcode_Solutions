class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr = [1, 1, 1, 1, 1]
        
        # n=1 is the base case
        # Time Complexity: O(10*len(arr)*n) ; Space Complexity: O(1)
        # After the base case, the value at pos i is the sum of the terms
        # after it
        for num in range(1, n):
            for i in range(len(arr)):
                arr[i] = sum(arr[i:])
        return sum(arr)
            