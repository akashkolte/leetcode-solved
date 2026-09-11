class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        freq = Counter(digits)
        res = 0

        for last in range(0, 10, 2):
            if freq[last] == 0:
                continue
            freq[last] -= 1

            for first in range(1, 10):
                if freq[first] == 0:
                    continue
                freq[first] -= 1
            
                for middle in range(10):
                    if freq[middle]: res += 1

                freq[first] += 1
            
            freq[last] += 1
        
        return res