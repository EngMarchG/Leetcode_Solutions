class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hmap = {}
        arr = []
        tt = len(nums)//3

        # Time complexity O(2N) Space complexity O(2N)
        for i in nums:
            if hmap.get(i,0):
                hmap[i] += 1
            else:
                hmap[i] = 1

            if hmap[i] > tt:
                    arr.append(i)
        return set(arr)