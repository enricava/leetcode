// https://leetcode.com/problems/word-ladder

class Solution(object):
    
    def isAdj(self, word1, word2):
        ok = True
        dif = False
        for k in range(len(word1)):
            if word1[k] != word2[k]:
                if dif:
                    ok = False
                    break
                if not dif:
                    dif = True
                
        return ok and dif
        
    
    def adj(self, word, wordList, visited):
        adj = []
        for i,x in enumerate(wordList):
            if visited[i] == 0 and self.isAdj(word, x):
                adj.append(i)
        return adj
            
    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not endWord in wordList:
            return 0
        visited = [0 for _ in wordList]
        queue = self.adj(beginWord, wordList, visited)
        level = 2
        while queue:
            level += 1
            k = len(queue)
            for _ in range(k):
                temp = queue.pop(0)
                visited[temp] == True
                if self.isAdj(wordList[temp], endWord):
                    return level
                else:
                    queue += self.adj(wordList[temp], wordList, visited)
        
        return 0
