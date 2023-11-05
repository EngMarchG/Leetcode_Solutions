class Solution:
    def judgeCircle(self, moves: str) -> bool:
        hmap = {}
        for move in moves:
            hmap[move] = hmap.get(move, 0) + 1

        if not hmap.get('L', 0) - hmap.get('R', 0) and not hmap.get('U', 0) - hmap.get('D', 0):
            return True