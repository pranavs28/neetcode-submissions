class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        
        e = defaultdict(list)
        for edge in edges:
            e[edge[0]].append(edge[1])
            e[edge[1]].append(edge[0])

        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            for node in e[i]:
                if node is not i:
                    dfs(node)
        
        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)

        return components

        