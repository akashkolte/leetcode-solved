class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        dist = float('inf')
        index1 = float('inf')
        index2 = float('inf')
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                index1 = i
            if wordsDict[i] == word2:
                index2 = i
            dist = min(abs(index2 - index1), dist)
        
        return dist
