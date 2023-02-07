# 최소 비용으로 모든 노드를 연결
import sys

input = sys.stdin.readline

# 컴퓨터의 수 N
N = int(input())

# 연결할 수 있는 선의 수 M
M = int(input())

answer = 0
edges = []

for _ in range(M):
    a,b,c = map(int, input().split())
    edges.append([a,b,c])
    
edges.sort(key=lambda x: x[2])

connection = set([edges[0][0]])

while len(connection) < N:
    for edge in edges:
        if edge[0] in connection and edge[1] in connection:
            continue
        
        if edge[0] in connection or edge[1] in connection:
            connection.update([edge[0], edge[1]])
            answer += edge[2]
            break
        
print(answer)
