class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        right = len(palindrome) - 1
        if right < 1:
            return ""
        
        left = 0
        
        
        # Time complexity O(N) Space comlexity O(1)
        while left < right:
            # You are guranteed a palindrome so no need to check left and right
            if palindrome[left] != "a":
                return palindrome[:left] + "a" + palindrome[left+1:]
            
            left += 1
            right -= 1
        
        # Repeated cases or odd lengths
        rep = 97
        right = len(palindrome) - 1
        while True:
            if palindrome[right] != chr(rep):
                return palindrome[:len(palindrome)-1] + chr(rep)
            rep += 1