class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, counts = 0, 0 
        while i < len(flowerbed)-1:
            if flowerbed[i] != 1 and flowerbed[i+1] != 1:
                if i > 0 and flowerbed[i-1] == 1:
                    i += 1
                    continue
                flowerbed[i] = 1
                counts += 1
            i += 1
        if not flowerbed[i] and not flowerbed[i-1]:
            counts += 1

        return counts >= n
