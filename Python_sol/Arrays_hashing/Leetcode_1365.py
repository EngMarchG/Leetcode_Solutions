class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num,0)+1 
        
        ans = []
        ordered_list = sorted(nums, reverse=True)
        for i in range(len(nums)):
            for j in range(len(ordered_list)):
                if nums[i] == ordered_list[j]:
                    ans.append(len(nums) - j - hmap[nums[i]])
                    break

        return ans