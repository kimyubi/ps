# 전위 탐색: 부모, 왼쪽, 오른쪽 
# 후위 탐색: 왼쪽, 오른쪽, 부모
from sys import setrecursionlimit
setrecursionlimit(10000)

class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.left = None
        self.right = None

def addNode(parent, child):
    # 왼쪽 서브트리에 노드 추가
    if child.x < parent.x:
        if parent.left == None:
            parent.left = child
        else:
            addNode(parent.left, child)
    # 오른쪽 서브트리에 노드 추가
    else:
        if parent.right == None:
            parent.right = child
        else:
            addNode(parent.right, child)
            
def preorder(node, pre_answer):
    if node == None:
        return
    
    pre_answer.append(node.id)
    preorder(node.left, pre_answer)
    preorder(node.right, pre_answer)
    
def postorder(node, post_answer):
    if node == None:
        return
    
    postorder(node.left, post_answer)
    postorder(node.right, post_answer)
    post_answer.append(node.id)

def solution(nodeinfo):
    pre_answer, post_answer = [], []
    node_list = []

    for idx, info in enumerate(nodeinfo):
        info.append(idx + 1)
        
    for x, y, idx in sorted(nodeinfo, key = lambda x : (-x[1], x[0])):
        node_list.append(Node(idx, x, y))
        
    root = node_list[0]
    for node in node_list[1:]:
        addNode(root, node)
        
    preorder(root, pre_answer)
    postorder(root, post_answer)
    
    return [pre_answer, post_answer]