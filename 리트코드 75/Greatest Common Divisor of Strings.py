# 2: 13 ~ 2: 33
# 최대 공약 문자
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_len, str2_len = len(str1), len(str2)
        if str1_len == str2_len:
            if str1 != str2:
                return ''
            else:
                return str1

        shortest_str = str1 if str1_len < str2_len else str2
        tmp, answer = '', ''
        for c in shortest_str:
            tmp += c
            tmp_str1 = str1.replace(tmp, '')
            tmp_str2 = str2.replace(tmp, '')

            if not tmp_str1 and not tmp_str2:
                answer = tmp

        return answer if answer else ''            


        
        