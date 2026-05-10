class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count_0 = students.count(0)
        count_1 = students.count(1)

        n = len(students)
        res = n
        for sandwich in sandwiches:
            if sandwich == 0:
                if count_0 > 0:
                    count_0 -= 1
                    res -= 1
                else:
                    return res
            else:
                if count_1 > 0:
                    count_1 -= 1
                    res -= 1
                else:
                    return res
        return res




        