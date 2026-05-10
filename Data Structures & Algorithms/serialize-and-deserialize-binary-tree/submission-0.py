class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        serial = []
        q = deque([root])
        
        while q:
            curr = q.popleft()
            if curr:
                serial.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                serial.append("null")
        
        result = ",".join(serial)
        return result

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        array = data.split(",")
        root = TreeNode(int(array[0]))
        q = deque([root])
        i = 1
        
        while q and i < len(array):
            curr = q.popleft()
            
            if array[i] != "null":
                curr.left = TreeNode(int(array[i]))
                q.append(curr.left)
            i += 1
            
            if i < len(array) and array[i] != "null":
                curr.right = TreeNode(int(array[i]))
                q.append(curr.right)
            i += 1
            
        return root