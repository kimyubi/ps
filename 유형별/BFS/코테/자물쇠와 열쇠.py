def rotate(key):
    return [x for x in zip(*key[::-1])]
    
def make_new_lock(lock, M, N):
    new_lock = [[0] * (2 * M + N) for _ in range(2 * M + N)]
    for i in range(N):
        for j in range(N):
            new_lock[M + i][M + j] = lock[i][j]
    return new_lock

def attatch(x, y, M, key, lock):
    for i in range(M):
        for j in range(M):
            lock[x + i][y + j] += key[i][j]
            
def detach(x, y, M, key, lock):
    for i in range(M):
        for j in range(M):
            lock[x + i][y + j] -= key[i][j]

def check_match(lock, M, N):
    for i in range(N):
        for j in range(N):
            if lock[M + i][M + j] != 1:
                return False
    return True

def solution(key, lock):
    M, N = len(key), len(lock)
    # lock 재배치
    lock = make_new_lock(lock, M, N)
    
    for i in range(4):
        key = rotate(key)    
        for i in range(1, M + N):
            for j in range(1, M + N):
                attatch(i, j, M, key, lock)
                if check_match(lock, M, N):
                    return True
                detach(i, j, M, key, lock)
    return False