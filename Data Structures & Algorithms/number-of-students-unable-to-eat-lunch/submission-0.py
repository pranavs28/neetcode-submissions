class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        stack_top = 0
        n = len(students)
        hungry_students = n

        for sandwich in sandwiches:
            count = 0
            while count < n and q[0] != sandwich:
                curr = q.popleft()
                q.append(curr)
                count += 1
            
            if q[0] == sandwich:
                q.popleft()
                hungry_students -= 1
            else:
                break
        return hungry_students




        