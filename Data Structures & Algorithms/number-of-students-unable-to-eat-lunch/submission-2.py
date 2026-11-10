class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        x = len(students) ** 2
        y = 0
        while students and sandwiches and y < x :
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students[0])
                students.pop(0)
            y += 1
        return len(students)