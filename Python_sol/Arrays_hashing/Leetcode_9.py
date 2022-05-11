
#  Convert the integer to a string and initiate a loop
#  with 2 pointers till the middle with
#  Time Complexity: O(n+n/2) ; Space Complexity: O(n)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        for i in range(int(len(y)/2)):
            if y[i] != y[-1-i]:
                return 0
        return 1