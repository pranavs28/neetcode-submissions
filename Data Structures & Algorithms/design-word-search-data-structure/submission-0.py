class WordDictionary:

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.isWord = False

    def __init__(self):
        self.trie = self.TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.trie
        for w in word:
            if w not in curr.children:
                curr.children[w] = self.TrieNode()
            curr = curr.children[w]
        curr.isWord = True

        

    def search(self, word: str) -> bool:
        def dfs(word, curr):
            for i in range(len(word)):
                if word[i] == '.':
                    for child in curr.children.values():
                        if dfs(word[i+1:], child):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.isWord
        return dfs(word, self.trie)