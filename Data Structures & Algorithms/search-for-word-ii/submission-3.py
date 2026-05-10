class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        rows = len(board)
        cols = len(board[0])
        #build trie for word bank
        class TrieNode:
            def __init__(self, val, isWord=False):
                self.val = val
                self.isWord = isWord
                self.children = {}
        
        head = TrieNode('.', False)

        for word in words:
            curr = head
            for l in word:
                if l not in curr.children:
                    curr.children[l] = TrieNode(l)
                curr = curr.children[l]
            curr.isWord = True
        
        #dfs backtrack through grid, find words

        res = []
        visited = set()
        def dfs(r, c, board, curr_string, trie):
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visited or board[r][c] not in trie:
                return
            
            if trie[board[r][c]].isWord == True:
                trie[board[r][c]].isWord = False
                res.append(curr_string + board[r][c])
            
            visited.add((r,c))
            for r_mod, c_mod in [[-1,0], [1,0], [0, -1], [0,1]]:
                dfs(r + r_mod, c + c_mod, board, curr_string + board[r][c], trie[board[r][c]].children)
            visited.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,board,"",head.children)
        
        return res


        