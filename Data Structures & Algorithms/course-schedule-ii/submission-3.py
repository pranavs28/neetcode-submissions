class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 0 = not visited, 1 = visiting, 2 = visited
        visit_status = [0] * numCourses

        #process adjacency list into hash map
        prereq_map = defaultdict(list)
        for prereq in prerequisites:
            prereq_map[prereq[1]].append(prereq[0])
        
        self.coursepath = []
        self.iscycle = False
        def dfs(i):
            if visit_status[i] == 1:
                self.iscycle = True
                return
            
            if visit_status[i] == 2:
                return
            
            visit_status[i] = 1

            for prereq in prereq_map[i]:
                dfs(prereq)
            self.coursepath.append(i)
            visit_status[i] = 2
            
        
        for i in range(numCourses):
            if visit_status[i] != 2:
                dfs(i)
                if self.iscycle:
                    return []

        return self.coursepath[::-1]

        