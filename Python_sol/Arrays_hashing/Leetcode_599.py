class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hmap = {}
        curr = float("inf")
        word = []

        for pos in range(len(list1)):
            hmap[list1[pos]] = pos
        
        for pos in range(len(list2)):
            if hmap.get(list2[pos], -1 ) != -1:
                hmap[list2[pos]] += pos
                if hmap[list2[pos]] == curr:
                    word.append(list2[pos])
                elif hmap[list2[pos]] < curr:
                    curr = hmap[list2[pos]]
                    word = [list2[pos]]

        return word