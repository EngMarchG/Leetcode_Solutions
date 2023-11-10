class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {x:i+1 for i,x in enumerate(nums2)}
        ans = []

        for num in nums1:
            temp = len(ans)
            for i in range(hmap[num],len(nums2)):
                if nums2[i] > num:
                    ans.append(nums2[i])
                    break
            if temp == len(ans):
                ans.append(-1)
        
        return ans
        