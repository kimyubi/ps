# 3:32 ~ 3: 35
class Solution(object):
    def reverseWords(self, s):
        reversed_s = s.split()[::-1]
        return ' '.join(reversed_s)
        