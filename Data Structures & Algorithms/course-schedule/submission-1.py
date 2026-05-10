class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses
        prereq_dict = defaultdict(list)
        for prereq in prerequisites:
            prereq_dict[prereq[0]].append(prereq[1])
        self.possible = True
        def dfs(i):
            if visited[i] == 1:
                self.possible = False
                return
            if visited[i] == 2:
                return
            else:
                visited[i] = 1
                for prereq in prereq_dict[i]:
                        dfs(prereq)
                visited[i] = 2
                return
        
        for i in range(numCourses):
                if self.possible:
                    dfs(i)
        return self.possible