class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {}
        count[0] = 1
        ans = tot = 0

        for num in nums:
            tot += num
            modulus = tot % k
            ans += count.get(modulus,0)
            count[modulus] = count.get(modulus,0) + 1
            
        print(count)
        return ans