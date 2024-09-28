class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rankings = sorted(score, reverse=True)
        ranking_map = {}
        
        for i, rank in enumerate(rankings):
            ranking_map[rank] = i + 1
        hmap = {1:"Gold Medal", 2:"Silver Medal", 3:"Bronze Medal"}
        
        ans = []
        for i, rank in enumerate(score):
            ans.append(hmap.get(ranking_map[rank], str(ranking_map[rank])))

        return ans