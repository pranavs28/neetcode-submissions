class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        class TrieNode:
            def __init__(self, val, isWord=False):
                self.val = val
                self.isWord = isWord
                self.children = {}
        
        trie = TrieNode('.')
        for word in wordDict:
            curr = trie
            for w in word:
                if w not in curr.children:
                    curr.children[w] = TrieNode(w)
                curr = curr.children[w]
            curr.isWord = True

        memo = [-1] * n
        
        def can_break(i):
            if i == n:
                return 1

            if memo[i] != -1:
                return memo[i]
            
            curr = trie
            index = i
            while index < n:
                if s[index] in curr.children:
                    if curr.children[s[index]].isWord:
                        if can_break(index + 1):
                            memo[i] = 1
                            return 1
                    
                    curr = curr.children[s[index]]
                    index += 1
                else:
                    break
            memo[i] = 0
            return 0
            
        return True if can_break(0) else False


