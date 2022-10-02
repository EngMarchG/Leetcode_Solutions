class Solution:
    def longestPalindrome(self, s: str) -> int:
        hmap = {}
        maxi = 0
        
        # Time complexity O(N) Space complexity O(set(N))
        # Create a hashmap of each letter in the string
        # and add to the count every 2
        for letter in s:
            if hmap.get(letter, 0):
                hmap[letter] += 1
                if not hmap[letter] % 2:
                    maxi += 2
            else:
                hmap[letter] = 1
        
        
        for num in hmap.values():
            if num % 2:
                return maxi + 1
        
        return maxi
            