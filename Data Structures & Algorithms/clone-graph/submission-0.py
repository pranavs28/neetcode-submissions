"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = {}
        if node is None:
            return None
        def dfs(node):
            if node is None or node.val in nodes:
                return
            
            new_node = Node(node.val)
            nodes[node.val] = new_node
            for neighbor in node.neighbors:
                if neighbor.val not in nodes:
                    dfs(neighbor)
                new_node.neighbors.append(nodes[neighbor.val])
            nodes[node.val] = new_node

        dfs(node)
        return nodes[1]
                


            
        