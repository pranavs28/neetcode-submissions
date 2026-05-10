class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses
        
        self.possible = True
        def dfs(i):
            if visited[i] == 1:
                self.possible = False
                return
            if visited[i] == 2:
                return
            else:
                visited[i] = 1
                for prereq in prerequisites:
                    if prereq[0] == i:
                        dfs(prereq[1])
                visited[i] = 2
                return
        
        for i in range(numCourses):
                if self.possible:
                    dfs(i)
        return self.possible