"""
Given a set of N intervals denoted by 2D array A of size N x 2, 
the task is to find the length of maximal set of mutually disjoint intervals.

Two intervals [x, y] & [p, q] are said to be disjoint 
if they do not have any point in common.

Return a integer denoting the length of maximal set of 
mutually disjoint intervals.

Constraints:
1 <= N <= 105
1 <= A[i][0] <= A[i][1] <= 109
"""

def exclusive(arr):
    arr.sort(key=lambda x: arr[1])

    prev_s, prev_e = arr[0]
    count = 1

    for s, e in arr:
        if s <= prev_e:
            pass
        else:
            prev_s, prev_e = s, e
            count += 1

    return count