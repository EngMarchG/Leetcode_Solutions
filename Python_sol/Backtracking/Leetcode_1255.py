class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        hmap = {}
        freq = {}
        self.ans = 0

        for i, letter in enumerate(letters):
            if not hmap.get(letter, 0):
                hmap[letter] = score[ord(letter)-97]
            freq[letter] = freq.get(letter, 0) + 1

        self.backtrack(words, hmap, freq, 0, 0)
        return self.ans

    def backtrack(self, words, hmap, freq, index, curr_score):
        self.ans = max(self.ans, curr_score)
        for i in range(index, len(words)):
            temp = 0
            valid = True
            occur = {}
            for letter in words[i]:
                if hmap.get(letter, -1) == -1 or freq.get(letter, 0) < occur.get(letter, 0) + 1:
                    valid = False
                    break
                temp += hmap[letter]
                occur[letter] = occur.get(letter, 0) + 1
            if valid:
                for letter in occur:
                    freq[letter] -= occur[letter]
                self.backtrack(words, hmap, freq, i + 1, curr_score + temp)
                for letter in occur:
                    freq[letter] += occur[letter]