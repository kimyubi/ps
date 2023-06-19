def solution(n, s, a, b, fares):
    INF = 100000 * n + 1
    graph = [[INF] * (n + 1) for _ in range (n + 1)]
    def floyd_warshall():
        for k in range(1, n + 1):
            for a in range(1, n + 1):
                for b in range(1, n + 1):
                    if a == b:
                        graph[a][b] = 0
                    
                    else:
                        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
                        
        
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
        
    floyd_warshall()
                        
    return min([graph[s][i] + graph[i][a] + graph[i][b] for i in range(n + 1)])