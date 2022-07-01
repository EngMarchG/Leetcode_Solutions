"""
Given an integer array A of size N consisting of unique integers 
from 1 to N. You can swap any two integers atmost B times.

Return the largest lexicographical value array that can 
be created by executing atmost B swaps.

Constraints:
1 <= N <= 106
1 <= B <= 109

https://www.interviewbit.com/problems/largest-permutation/
"""

def max_perm(arr, B):
    i = 0
    maxi = len(arr)
    dict = {x: i for i, x in enumerate(arr)}

    while B and i < len(arr):
        j = dict[maxi]
        if i == j:
            pass
        else:
            B -= 1
            arr[i], arr[j] = arr[j], arr[i]
            dict[arr[i]], dict[arr[j]] = dict[arr[j]], dict[arr[i]]
        
        i += 1
        maxi -= 1
    
    return arr