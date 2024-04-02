class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time complexity O(n + set(n)log(set(n))) & space complexity O(set(n))
        hmap = {}

        for num in nums:
            hmap[num] = hmap.get(num,0) + 1

        ans = []
        for key, val in hmap.items():
            ans.append([val, key])
        ans.sort(reverse=True)

        return [ans[num][1] for num in range(k)]