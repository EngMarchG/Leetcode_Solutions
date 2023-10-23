class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        needed = int(len(arr)*0.05)
        
        return sum(arr[needed:-needed])/len(arr[needed:-needed])
