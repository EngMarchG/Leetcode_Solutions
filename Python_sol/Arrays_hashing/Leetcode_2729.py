class Solution:
    def isFascinating(self, n: int) -> bool:
        return sorted(f'{str(n)}{str(n*2)}{str(n*3)}') == "123456789"
        