class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coords = {(0, 0)}
        x, y = 0, 0

        for pos in path:
            if pos == "N":
                y += 1
            elif pos == "S":
                y -= 1
            elif pos == "E":
                x -= 1
            else:
                x += 1
                
            if (x, y) in coords:
                return True
            coords.add((x, y))
        return False
