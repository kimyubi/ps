import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]


tetromino = [[1,1,1,1],[]]
