class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hmap = {x:0 for x in jewels}

        for stone in stones:
            if hmap.get(stone,-1) != -1:
                hmap[stone] += 1
            
        return sum(hmap.values())