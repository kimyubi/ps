from collections import deque
import copy

# 엄지손가락은 상하 좌우 4가지 방향으로만 이동할 수 있다.
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

keypad = [['1','2','3'],
          ['4','5','6'],
          ['7','8','9'],
          ['*','0','#']]

r, c = len(keypad), len(keypad[0])

direction = {"left": "L", "right": "R"}
origin_visited = [[0] * len(row) for row in keypad]

    
def bfs(cur_number, target_number):
    visited = copy.deepcopy(origin_visited)
    queue = deque()
    for i in range(r):
        for j in range(c):
            if keypad[i][j] == cur_number:
                queue.append([i,j])
                break
                
    while queue:
        x,y = queue.popleft()
        if keypad[x][y] == str(target_number):
            return visited[x][y]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                queue.append([nx, ny])
                # 키패드 이동 한 칸은 거리로 1에 해당한다.
                visited[nx][ny] = visited[x][y] + 1
        

def solution(numbers, hand):
    answer = ''
    cur_left_hand, cur_right_hand = '*', '#'
    for number in numbers:
        # 왼손 엄지손가락을 사용해야 하는 키패드
        if number in (1,4,7):
            answer += 'L'
            cur_left_hand = str(number)
            continue
            
        # 오른손 엄지손가락을 사용해야 하는 키패드 
        elif number in (3,6,9):
            answer += 'R'
            cur_right_hand = str(number)
            continue
        
        # 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 
        # 더 가까운 엄지손가락을 사용한다.
        else:
            distance_of_left = bfs(cur_left_hand, number)
            distance_of_right = bfs(cur_right_hand, number)
          
            # 왼손 엄지 손가락이 더 가까운 경우
            if distance_of_left < distance_of_right:
                answer += 'L'
                cur_left_hand = str(number)
                
            # 오른손 엄지 손가락이 더 가까운 경우
            elif distance_of_left > distance_of_right:
                answer += 'R'
                cur_right_hand = str(number)
                
            # 두 엄지손가락의 거리가 같은 경우
            else:
                answer += direction[hand]
                
                if hand == "left":
                    cur_left_hand = str(number)
                else:
                    cur_right_hand = str(number)
                
    return answer