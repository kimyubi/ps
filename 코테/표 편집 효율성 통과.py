def solution(n, k, commands):
    answer = ['O'] * n
    
    dic = { i : [i - 1, i + 1]  for i in range(n)}
    
    dic[0] = [None, 1]
    dic[n - 1] = [n - 2, None]
    stack = []
    
    for command in commands:
        if command == 'C':
            answer[k] = 'X'
            
            prev, next = dic[k]
            stack.append([prev, k, next])
            
            # 마지막 행을 삭제하는 경우
            if next == None:
                dic[prev][1] = None
                k = prev
            # 첫 행을 삭제하는 경우
            elif prev == None:
                dic[next][0] = None
                k = next
            # 중간 행을 삭제하는 경우
            else:
                dic[prev][1] = next
                dic[next][0] = prev
                k = next
            
                
        elif 'Z' == command:
            prev, now, next = stack.pop()
            answer[now] = 'O'
            
            # 마지막 행을 복구하는 경우
            if next == None:
                dic[prev][1] = now
            # 첫 행을 복구하는 경우
            elif prev == None:
                dic[next][0] = now
            # 중간 행을 복구하는 경우
            else:
                dic[prev][1] = now
                dic[next][0] = now
                
        else:
            c, num = command.split(' ')
            num = int(num)
            
            for _ in range(num):
                if c == 'D':
                    k = dic[k][1]
                else:
                    k = dic[k][0]
        
    return ''.join(answer)