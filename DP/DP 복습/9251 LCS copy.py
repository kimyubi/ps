import sys
input = sys.stdin.readline

s1 = input()
s2 =  input()

s1_len = len(s1)
s2_len = len(s2)

dp = [[''] * (s2_len + 1) for _ in range(s1_len + 1)]

s1, s2 = ' ' + s1, ' ' + s2
for i in range(1, s1_len + 1):
    for j in range(1, s2_len + 1):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i-1][j-1] + s1[i]
        
        
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
            
print(dp[-1][-1])