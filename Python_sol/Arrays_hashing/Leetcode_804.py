class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        arrLetter = [chr(x) for x in range(97, 97+26)]
        arrMorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        hmap = {}
        for x in range(len(arrMorse)):
            hmap[arrLetter[x]] = arrMorse[x]

        ans = []
        for x in range(len(words)):
            temp = []
            for letter in words[x]:
                temp.append(hmap[letter])
            ans.append("".join(temp))
        
        return len(set(ans))
        