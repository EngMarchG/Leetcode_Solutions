class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Time Complexity: O(n) Space Complexity: O(1)
        
        targ = tickets[k]
        tot = 0
        
        for x, ticket in enumerate(tickets):
            if ticket < targ:
                tot += ticket
            else:
                if x > k:
                    tot += targ-1
                else:
                    tot += targ
        return tot