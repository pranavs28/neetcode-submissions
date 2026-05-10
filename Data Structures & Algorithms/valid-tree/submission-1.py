class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        visited = set()

        e = defaultdict(list)
        for edge in edges:
            e[edge[0]].append(edge[1])
            e[edge[1]].append(edge[0])


        def dfs(i, parent):
            if i in visited:
                return False
            
            visited.add(i)
            for node in e[i]:
                if node is not parent:
                    isTree = dfs(node, i)
                    if not isTree:
                        return False
            return True
        
        return dfs(0, 0) and len(visited) == n