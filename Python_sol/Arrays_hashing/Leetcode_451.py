class Solution:
    def frequencySort(self, s: str) -> str:
        hmap = {}
        for ele in s:
            if hmap.get(ele, 0):
                hmap[ele] += 1
            else:
                hmap[ele] = 1
        hmap2 = {}
        
        for ele in hmap.keys():
            
            if hmap2.get(hmap[ele],0):                
                hmap2[hmap[ele]].append(ele)
            else:
                hmap2[hmap[ele]] = [ele]
        ans = ""
        arr = sorted(hmap2.keys(), reverse=True)
        for ele in arr:
            for em in hmap2[ele]:
                ans += em*ele
        return ans