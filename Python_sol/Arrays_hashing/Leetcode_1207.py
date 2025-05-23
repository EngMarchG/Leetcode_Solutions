class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = {}
        for num in arr:
            seen[num] = seen.get(num, 0) + 1

        if len(seen.values()) == len(set(seen.values())):
            return True
        return False