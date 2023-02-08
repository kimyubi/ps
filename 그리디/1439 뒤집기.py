import sys
input = sys.stdin.readline

s = list(map(int, input().rstrip()))
flag = s[0]
ans = [0,0]
ans[s[0]] = 1


for i in range(1,len(s)):
    if s[i] == flag:
        continue
    else:
        flag = s[i]
        ans[flag] += 1
    
print(ans)