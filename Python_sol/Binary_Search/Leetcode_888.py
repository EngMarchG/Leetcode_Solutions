class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # Time Complexity: O(n + 2m + nlogm) Space Complexity: O(1)
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        bobSizes.sort()  
        
        for x in aliceSizes:
            currTar = x - diff
            p1 = 0
            p2 = len(bobSizes) - 1
            
            while p1 <= p2:
                mid = (p1 + p2) // 2
                if bobSizes[mid] == currTar:
                    return [x, currTar]
                elif bobSizes[mid] < currTar:
                    p1 = mid + 1
                else:
                    p2 = mid - 1