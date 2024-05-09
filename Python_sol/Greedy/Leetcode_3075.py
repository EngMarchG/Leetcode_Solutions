class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        selects = 0
        max_hp = 0

        happiness.sort(reverse=True)

        for happy in happiness:
            metric = happy - selects 
            if metric <= 0 or selects == k:
                break 
            max_hp += metric
            selects += 1

        
        return max_hp