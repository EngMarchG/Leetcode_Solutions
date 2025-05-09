class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        curr_sum = float(inf)

        for i in range(len(arr)-1):
            temp_sum = abs(arr[i+1] - arr[i])
            if temp_sum < curr_sum:
                curr_sum = temp_sum
                ans = [[arr[i], arr[i+1]]]
            elif temp_sum == curr_sum:
                ans.append([arr[i], arr[i+1]])

        return ans