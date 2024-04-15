class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        hmap = {}
        for student in students:
            hmap[student] = hmap.get(student,0) + 1

        for i, sandwich in enumerate(sandwiches):
            if not hmap[sandwich]:
                return i
            hmap[sandwich] -= 1
        
        return 0