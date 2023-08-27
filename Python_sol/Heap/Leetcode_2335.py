class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # Time Complexity: O(nlogn) Space Complexity: O(1)
        # round() doesn't work since it rounds down when the decimal is 0.5 or less

        amount = sorted(amount, key=lambda x: -x)
        #amount = sorted(amount, reverse=True)
        diff = sum(amount[1:]) - amount[0]

        if diff <= 0:
            return amount[0]
        elif diff > 0:
            return amount[0] + math.ceil(diff / 2)



# Without using math.ceil
# class Solution:
#     def fillCups(self, amount: List[int]) -> int:
#         amount = sorted(amount, key=lambda x: -x)
#         diff = sum(amount[1:]) - amount[0]

#         if diff <= 0:
#             return amount[0]
#         elif diff > 0:
#             remain = diff / 2
#             if remain - int(remain) > 0:
#                 remain = int(remain) + 1
#             return amount[0] + int(remain)