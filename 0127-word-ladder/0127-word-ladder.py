from typing import List 
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = [beginWord] + wordList
        matrix = [set() for _ in range(len(wordList))]
        for idx1 in range(len(wordList)):
            word1 = wordList[idx1] 
            for idx2 in range(idx1+1, len(wordList)):
                word2 = wordList[idx2]
                diff = 0
                for i in range(len(word1)):
                    if diff > 1:
                        break
                    diff += word1[i] != word2[i]
                if diff == 1:
                    matrix[idx1].add(idx2)
                    matrix[idx2].add(idx1)
        
        queue = deque([(0, 0)])
        visited = {0}
        while queue:
            index, depth = queue.popleft()
            if wordList[index] == endWord:
                return depth + 1
            for neighbor in matrix[index]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
                    
        return 0
