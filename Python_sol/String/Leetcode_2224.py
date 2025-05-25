class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        possibilities = [15, 5, 1]

        ans = abs(int(current[:2]) - int(correct[:2]))
        minute = int(correct[3:]) - int(current[3:])
        if minute < 0:
            ans -= 1
            minute = 60 - abs(minute) 
        for trial in possibilities:
            if minute >= trial:
                ans += minute // trial
                minute = minute % trial
        return ans