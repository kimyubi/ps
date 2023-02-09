import sys
import heapq
input = sys.stdin.readline

# 수업의 개수 n
n = int(input())
lectures = []

for _ in range(n):
    s, t = map(int, input().split())
    lectures.append([s,t])

lectures.sort()

room = []
heapq.heappush(room, lectures[0][1])


for i in range(1, n):
    # 강의실 그대로 사용
    if room[0] <= lectures[i][0]:
        heapq.heappop(room)
        heapq.heappush(room, lectures[i][1])
        
    # 새 강의실 개설
    else:
        heapq.heappush(room, lectures[i][1])



print(len(room))
