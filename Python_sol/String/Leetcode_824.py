class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        ans = []
        letters = 0

        for word in sentence.split(" "):
            letters += 1
            if word[0].lower() in vowels:
                temp = word + "ma"
            else:
                temp = word[1:] + word[0] + "ma"
            
            ans.append(temp + "a" * letters)
        
        return " ".join(ans)

