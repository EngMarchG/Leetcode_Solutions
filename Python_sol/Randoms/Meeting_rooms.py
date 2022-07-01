"""
Given an 2D integer array A of size N x 2 denoting 
time intervals of different meetings.

Where:
A[i][0] = start time of the ith meeting.
A[i][1] = end time of the ith meeting.

Find the minimum number of conference rooms required 
so that all meetings can be done.

Constraints:
1 <= N <= 10
0 <= A[i][0] < A[i][1] <= 2 * 109
"""
def meeting(A):
    data = []
    for r, c in A:
        data.append((r, +1))
        data.append((c, -1))

    data.sort()

    room = 0
    lowest = 0
    for _, slot in data:
        room += slot
        lowest = max(room, lowest)
    return lowest