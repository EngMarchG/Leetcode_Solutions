class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        separators = ['.', ',', ';', '?', '!']
        for sep in separators:
            paragraph = paragraph.replace(sep, " ")

        paragraph = paragraph.split()
        hmap = {}

        ans = ["",0]
        for word in paragraph:
            cword = word.lower()
            cword = cword.rstrip(".;!?',")
            if cword not in banned:
                hmap[cword] = hmap.get(cword, 0) + 1
                if hmap[cword] > ans[1]:
                    ans[0] = cword
                    ans[1] += 1
        
        return ans[0]