# 처음 표의 행 개수를 나타내는 정수 n 
# 처음에 선택된 행의 위치를 나타내는 정수 k
# 수행한 명령어들이 담긴 문자열 배열 cmd
def solution(n, k, commands):
    answer = ''
    rows = [i for i in range(n)]
    removed_row = []
    
    for command in commands:
        # 현재 선택된 행에서 X칸 위에 있는 행을 선택
        if "U" in command:
            k -= int(command.split(" ")[1])
        # 현재 선택된 행에서 X칸 아래에 있는 행을 선택
        elif "D" in command:
            k += int(command.split(" ")[1])
        # 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택
        # 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택
        elif "C" in command:
            t = len(rows) - 1
            removed_row.append([rows.pop(k), k])
            if k == t:
                k -= 1
        else:
            value, index = removed_row.pop()
            rows.insert(index, value)
            if index <= k:
                k += 1
                
    for x in range(n):
        if x in rows:
            answer += 'O'
        else:
            answer += 'X'
            
    return answer