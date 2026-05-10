class PrefixTree:

    class TrieNode():

        def __init__(self):
            self.children = {}
            self.isWord = False

    def __init__(self):
        self.trie = self.TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.trie
        for w in word:
            if w not in curr.children:
                curr.children[w] = self.TrieNode()
            curr = curr.children[w]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.trie
        for w in word:
            if w not in curr.children:
                return False
            else:
                curr = curr.children[w]
        return curr.isWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for w in prefix:
            if w not in curr.children:
                return False
            else:
                curr = curr.children[w]
        return True
        
        