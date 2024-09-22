class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hmap = {}
        ans = [[0,0,0]]

        for i, num in enumerate(nums):
            if not hmap.get(num,0):
                hmap[num] = [1, i]
            else:
                hmap[num][0] += 1

            if ans[0][0] < hmap[num][0]:
                ans = [[hmap[num][0], num, i]]
            elif ans[0][0] == hmap[num][0]:
                ans.append([hmap[num][0], num, i])
        
        final_ans = float(inf)
        for answer in ans:
            final_ans = min(final_ans, answer[2] - hmap[answer[1]][1] + 1)
        
        return final_ans



# class Solution:
#     def findShortestSubArray(self, nums: List[int]) -> int:
#         hmap = {}
#         ans = [[0,0,0]]

#         for i, num in enumerate(nums):
#             hmap[num] = hmap.get(num,0) + 1
#             if ans[0][0] < hmap[num]:
#                 ans = [[hmap[num], num, i]]
#             elif ans[0][0] == hmap[num]:
#                 ans.append([hmap[num], num, i])
        
#         final_ans = float(inf)
#         for answer in ans:
#             i = 0
#             while nums[i] != answer[1]:
#                 i += 1
#             final_ans = min(final_ans, answer[2] - i + 1)
        
#         return final_ans
