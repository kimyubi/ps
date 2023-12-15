class Solution:
    def compress(self, chars: List[str]) -> int:
        group = []
        s = ''
        for char in chars:
            if not s:
                s += char
                continue

            if s[-1] != char:
                group.append(s)
                s = char
            else:
                s += char
        group.append(s)

        tmp = ''
        for item in group:
            key, value = item[0], len(item)
            tmp += key
            if 1 < value:
                tmp += str(value)
        
        chars.clear()
        chars.extend(list(tmp))
        return len(chars)
            






                

        