class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        ans = money - sum(prices[:2])

        if ans >= 0:
            return ans
        return money




"""class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        arr = [float("inf"),float("inf")]
        for price in prices:
            if arr[1] > price:
                arr[0] = min(arr[0],arr[1])
                arr[1] = price
            else:
                arr[0] = min(price,arr[0])

        ans = money - sum(arr)
        if ans >= 0:
            return ans

        return money"""