"""
Given N bulbs, either on (1) or off (0)
Turning on i-th bulb causes all remaining bulbs on the right to flip.
Find the min numbers of switches to turn all of the bulbs on.

Constraints:
1 <= N <= 1e5
A[i] = {0, 1}

https://www.interviewbit.com/problems/interview-questions/
"""

def  bulbs(bulb):
    cost = 0

    for bul in bulb:
        if cost % 2 != 0:
            bul = not bul

        if bul % 2 == 1:
            continue
        else:
            cost += 1
    return cost

print(bulbs([0,1,0,0]))
