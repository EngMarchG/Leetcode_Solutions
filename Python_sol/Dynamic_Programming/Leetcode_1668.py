class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = i = temp = 0
        size = len(word)

        # Sliding window approach
        while i <= len(sequence)-size:
            print(sequence[i:i+size])
            if word == sequence[i:i+size]:
                temp += 1
                i += size
            else:
                ans = max(ans, temp)
                if temp:
                    revert = 0

                    # Backtrack in case the skipped characters are the same as the first character of the word
                    # To not miss any possible repeating word
                    while revert < size:
                        if i > 0 and sequence[i-1]==word[0]:
                            i -= 1
                            revert += 1
                        else:
                            i -= 1 # Extra decrement to account for the increment in the next iteration
                            break
                i += 1
                temp = 0

        return max(ans, temp)