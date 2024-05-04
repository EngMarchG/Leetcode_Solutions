# Best solution
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1

        return boats


"""class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        left, right = 0, len(people) - 1
        temp = right

        while left <= right:
            right = self.binary_search(people, left, right, limit - people[left]) - 1
            if people[left] + people[right] <= limit:
                left += 1
            
            boats += temp - right
            temp = right

        return boats

    def binary_search(self, people, left, right, target):
        while left < right:
            mid = left + (right - left + 1) // 2
            if people[mid] <= target:
                left = mid
            else:
                right = mid - 1
        return left"""