class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            if n==1:
                return 1
            return -1
        indexer = trust[0][1]
        maxi = 0

        hmap = {}
        hmap2 = {}
        for i in range(len(trust)):
            hmap[trust[i][0]] = trust[i][1]
            
            if hmap2.get(trust[i][1],0):
                hmap2[trust[i][1]] += 1
                if hmap2[trust[i][1]]>maxi:
                    maxi = hmap2[trust[i][1]]
                    indexer = trust[i][1]

            else:
                hmap2[trust[i][1]] = 1

        if hmap2[indexer]==n-1 and not hmap.get(indexer,0):
            return indexer
        return -1