T = int(input())
ans_list = []
for test_case in range(1, T + 1):
    ans = 0
    for x in list(map(int, input().split())):
    	if x % 2 != 0:
            ans += x
    ans_list.append("#"  +  str(test_case) + " "  +  str(ans))
   
print()
for ans in ans_list:
    print(ans)       
