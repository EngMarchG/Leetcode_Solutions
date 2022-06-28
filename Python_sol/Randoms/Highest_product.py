"""
Given an array of N integers,
find the highest product by multiplying
3 elements.

Constraints:
3 <= N <= 5^5

https://www.interviewbit.com/problems/highest-product/
"""

def max_prod(arr):
    sort_arr = sorted(arr)

    pos_max = sort_arr[-1] * sort_arr[-2] * sort_arr[-3]
    neg_pos_max = sort_arr[0] * sort_arr[1] * sort_arr[2]
    return max(pos_max, neg_pos_max)