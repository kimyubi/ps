# 3:03 ~ 3:24
class Solution(object):
    def reverseVowels(self, s):
        tmp = [c for c in s if c in 'aeiouAEIOU']
        return ''.join([c if c not in 'aeiouAEIOU' else tmp.pop() for c in s])

        
