class Solution:
    def minDeletions(self, s: str) -> int:
        hmap = {}

        for x in s:
            hmap[x] = hmap.get(x, 0) + 1

        # Convert the frequencies into a list and sort it
        freq_list = sorted(list(hmap.values()))
        ans = 0

        if len(freq_list) > 1:
            for x in range(1, len(freq_list)):
                if freq_list[x - 1] == freq_list[x]:
                    y = x
                    while freq_list[y] > 0 and y > 0:
                        if freq_list[y] == freq_list[y-1]:
                            freq_list[y - 1] -= 1
                            ans += 1
                        else:
                            break
                        y -= 1

        return ans
