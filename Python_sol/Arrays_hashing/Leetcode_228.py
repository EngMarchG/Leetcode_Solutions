class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        arr = []
        curr = nums[0]
        counts = 0

        # Time complexity O(N) Space complexity O(N)
        for i in range(1,len(nums)):
            if nums[i] - curr - counts == 1:
                counts += 1
                continue
            
            if counts:
                arr.append(f"{curr}->{nums[i-1]}")
            else:
                arr.append(f"{curr}")
            curr = nums[i]
            counts = 0

        if not counts:
            arr.append(f"{nums[-1]}")
        else:
            arr.append(f"{curr}->{nums[-1]}")
        
        return arr