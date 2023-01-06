class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        costs = sorted(costs)

        # Time complexity O(2N) Space complexity O(1)
        for cost in costs:
            if coins >= cost:
                coins -= cost
                count += 1
            else:
                break
        return count