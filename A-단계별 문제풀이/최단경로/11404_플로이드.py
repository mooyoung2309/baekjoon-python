import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = sys.maxsize
dosi = [[INF for _ in range(N+1)] for __ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    dosi[a][b] = min(c, dosi[a][b])

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                dosi[i][j] = 0
            else:
                dosi[i][j] = min(dosi[i][j], dosi[i][k] + dosi[k][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if dosi[i][j] == INF:
            print(0, end = ' ')
        else:
            print(dosi[i][j], end = ' ')
    print()