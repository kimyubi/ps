# 2:00 ~ 2:07
from collections import deque
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ''
        
        word1, word2 = deque(word1), deque(word2)
        while word1 or word2:
            if word1:
                answer += word1.popleft()
            if word2:
                answer += word2.popleft()

        return answer
    
    
# 개선한 코드
from itertools import zip_longest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join([c1 + c2 for c1, c2 in zip_longest(word1, word2, fillvalue= "")])