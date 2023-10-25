class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        s = s.replace("-","")

        divs = len(s)/k
        initial = len(s) % k
        if divs > int(divs):
            divs = int(divs)+1

        ans = []

        if initial:
            ans.append(s[:initial])

        else:
            ans.append(s[:k])
            initial = k
        
        for i in range(1,int(divs)):
            ans.append(f"-{s[initial:initial+k]}")
            initial += k

        return "".join(ans)