import sys
input = sys.stdin.readline

a = " " + input().rstrip()
b = " " + input().rstrip()

# LCS[i][j] : a의 i번째 문자열과 b의 j번째 문자열까지의 LCS
LCS = [[""] * len(b) for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            LCS[i][j] = LCS[i-1][j-1] + a[i]
        
        else:
            if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]
            
result = LCS[-1][-1]

print(len(result), result, sep="\n")
        
        