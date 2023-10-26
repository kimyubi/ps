from itertools import product
def solution(word):
    dic = []
    alpha = ['A','E','I','O','U']
    for i in range(1, 6):
        dic.extend(list(map(''.join, product(alpha, repeat = i))))
    dic.sort()
    return dic.index(word) + 1