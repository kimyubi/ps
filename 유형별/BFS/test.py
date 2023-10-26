a = [[1,2,3], [6,7]]

result = [x for x in zip(*a[::-1])]
print(result)