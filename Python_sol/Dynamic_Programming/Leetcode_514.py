class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        hmap = {}
        for i, letter in enumerate(ring):
            if not hmap.get(letter, 0):
                hmap[letter] = []
            hmap[letter].append(i)

        cycle = len(ring)
        dp = [[float('inf')] * cycle for _ in range(len(key))]
        for pos in hmap[key[0]]:
            dp[0][pos] = min(pos, cycle - pos) + 1

        for i in range(1, len(key)):
            for pos in hmap[key[i]]:
                for prev_pos in hmap[key[i-1]]:
                    clockwise = (pos - prev_pos) % cycle
                    counter_clockwise = (prev_pos - pos) % cycle
                    steps = min(clockwise, counter_clockwise)
                    dp[i][pos] = min(dp[i][pos], steps + dp[i-1][prev_pos] + 1)

        return min(dp[-1])