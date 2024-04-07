class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True

        hmap = {}
        for card in hand:
            hmap[card] = hmap.get(card, 0) + 1

        keys = sorted(hmap.keys())

        for i in range(len(keys)):
            if hmap[keys[i]] > 0:
                count = hmap[keys[i]]
                for j in range(groupSize):
                    if hmap.get(keys[i] + j, 0) < count:
                        return False
                    hmap[keys[i] + j] -= count

        return True