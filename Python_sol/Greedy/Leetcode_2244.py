class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        hmap = {}
        rounds = 0

        # Time complexity O(N+set(N)) Space complexity O(set(N))
        for i in tasks:
            if hmap.get(i, 0):
                hmap[i] += 1
            else:
                hmap[i] = 1
        
        for i in hmap.values():
            if i < 2:
                return -1
            elif i < 4:
                rounds += 1
            else:
                temp = i/3
                if temp-int(temp)==0.0:
                    rounds += int(temp)
                    continue
                # There are 3 cases 0.3333, 0.666, or 0
                # In both cases 0.333 and 0.666 we notice that we end up with 1
                # extra turn after going back once and dividing by 2 twice (for 0.333)
                # Or divding by 2 once (for 0.666)
                elif (temp-int(temp)) > 0.3:
                    rounds += 1 + int(temp)
                    continue

                temp = i/2
                if temp-int(temp)==0.0 or temp-int(temp)==0.5:
                    rounds += int(temp)
                else:
                    return -1
        return rounds
                
