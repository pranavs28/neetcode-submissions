class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()

        visit = set()
        wordList_set = set(wordList)
        visit.add(beginWord)

        q.append((beginWord, 1))
        if endWord not in wordList_set:
            return 0


        while q:
            curr_word, curr_dist = q.popleft()
            
            for i in range(len(curr_word)):
                for j in range(26):
                    sub_letter = chr(ord('a') + j)
                    sub_word = curr_word[:i] + sub_letter + curr_word[i+1:]

                    if sub_word == endWord:
                        return curr_dist + 1

                    if sub_word in wordList_set and sub_word not in visit:
                        q.append((sub_word, curr_dist + 1))
                        visit.add(sub_word)
            
        return 0
                    
        