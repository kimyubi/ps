class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        if not len_s:
            return True

        cnt = 0
        for c in t:
            if c == s[cnt]:
                cnt += 1
            
            if cnt == len_s:
                return True

        return False




    
        