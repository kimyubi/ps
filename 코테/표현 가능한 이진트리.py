# 살펴본 노드가 더미 노드라면, 문자열 뒤에 0을 추가한다.
# 살펴본 노드가 더미 노드가 아니라면, 문자열 뒤에 1을 추가한다.
def find_root(tree):     
    root_index = len(tree) // 2 -1 if len(tree) % 2 == 0 else len(tree) // 2 
    left, right = tree[0:root_index], tree[root_index + 1:]
    
    # 부모 노드가 0이면 자식 노드가 1이어서는 안된다. (처리 하기)
    if not tree[root_index]:
        if 1 in left or 1 in right:
            return 0
   
    if len(tree[0:root_index]) >= 3:
        find_root(tree[0:root_index])
    if len(tree[root_index + 1:]) >= 3:
        find_root(tree[root_index + 1:])
    
    return 1

def make_binary_tree(number):
    # 10진수를 2진수로 변환한다.
    binary_num = list(map(int, bin(number)[2:]))
    standard = 1
    print(binary_num)
    while 2 ** standard -1 < len(binary_num):
        standard += 1
    binary_num = [0] * (2 ** standard -1 - len(binary_num)) + binary_num

    root_index = len(binary_num) // 2 -1 if len(binary_num) % 2 == 0 else len(binary_num) // 2 
    print(binary_num[0:root_index], binary_num[root_index], binary_num[root_index + 1:])
    # root가 0이면 이진트리로 표현할 수 없다.
    if not binary_num[root_index]:
        return 0
    if not find_root(binary_num[0:root_index]):
        return 0
    if not find_root(binary_num[root_index + 1:]):
        return 0
    
    return 1

def solution(numbers):
    answer = []
    
    for number in numbers:
        if number == 1:
            answer.append(1)
        else:
            answer.append(make_binary_tree(number))
    return answer