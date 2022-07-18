N, K = map(int, input().split())

list = [i for i in range(1, N+1)]
sum = -1

result = []

while list:
    x = (sum + K) % len(list)
    result.append(str(list.pop(x)))
    sum = x -1

print('<' + ', '.join(result) +'>')