# 1:52 ~ 2:50
import sys
from collections import Counter
input = sys.stdin.readline

def row_sorting(row):
    sorted_row, result = [], []
    counter = Counter(row)
    
    for x in counter:
        # sorted_row = [수, 수의 등장 횟수]
        sorted_row.append([x, counter[x]])
        
    # 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다.
    sorted_row.sort(key=lambda x : (x[1], x[0]))
    
    for num, cnt in sorted_row:
        # 수를 정렬할 때 0은 무시해야 한다.
        if num != 0:
            result.extend([num, cnt])
        
    return result, len(result)


def rotate(arr):
    return list(zip(*arr[::-1]))

def solution():
    global answer, arr
    
    while True:  
        # R 연산:  열의 개수 <= 행의 개수인 경우
        if len(arr[0]) <= len(arr):
            sorted_arr = []
            max_len = 0
            for row in arr:
                result, sorted_arr_len = row_sorting(row)
                sorted_arr.append(result)
                max_len = max(max_len, sorted_arr_len)
                
            for row in sorted_arr:
                row_len = len(row)
                if row_len < max_len:
                    for _ in range(max_len - row_len):
                        row.append(0)
                        
            arr = sorted_arr
                    
        
        # L 연산
        else:
            tmp = arr
            max_len = 0
            for i in range(3):
                tmp = rotate(tmp)
                
            sorted_column = []
            while tmp:
                now = tmp.pop()
                result, sorted_column_len = row_sorting(now)
                sorted_column.append(result)
                max_len = max(max_len, sorted_column_len)
                
            for column in sorted_column:
                col_len = len(column)
                if col_len < max_len:
                    for _ in range(max_len - col_len):
                        column.append(0)
            
            result = []
            for sort_set in zip(*sorted_column):
                result.append(list(sort_set))
                
            arr = result
    
    
        answer += 1
        if r <= len(arr) and c <= len(arr[0]) and arr[r-1][c-1] == k:
                break 
        
        if answer == 101:
            answer = -1
            break
        
    



if __name__ == '__main__':
    r, c, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(3)]
    if r <= len(arr) and c <= len(arr[0]) and arr[r-1][c-1] == k:
        print(0)
    else:
        answer = 0
        solution()
        print(answer)