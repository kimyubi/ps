def find_root(tree):
    size = len(tree)
    if size == 1 or 1 not in tree or 0 not in tree:
        return 1
    
    root_index = size // 2
    if not tree[root_index]:
        return 0

    left, right = tree[:root_index], tree[root_index + 1:]
    return find_root(left) and find_root(right)

def make_binary_tree(number):
    binary_num = list(map(int, bin(number)[2:]))
    standard = 1
    while 2 ** standard -1 < len(binary_num):
        standard += 1
    binary_num = [0] * (2 ** standard -1 - len(binary_num)) + binary_num
    return find_root(binary_num)
 

def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(make_binary_tree(number))
    return answer