class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hmap = {}
        for card in deck:
            hmap[card] = hmap.get(card, 0) + 1
        
        sorted_arr = sorted(hmap.values())

        if sorted_arr[0] < 2:
            return False

        for divisor in range(2, sorted_arr[0]+1):
            if sorted_arr[0] % divisor:
                continue

            temp = True
            for card in sorted_arr:
                if card % divisor:
                    temp = False
                    break
                    
            if temp:
                return True
