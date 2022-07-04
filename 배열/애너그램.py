from collections import Counter

x = input()
y = input()
result = 0

cnt_x = Counter(x)
cnt_y = Counter(y)

new_cnt = (cnt_x - cnt_y) + (cnt_y - cnt_x)
for v in new_cnt.values():
    result += v
    
print(result)



