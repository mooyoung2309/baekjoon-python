import sys
import collections
input = sys.stdin.readline

#총 6개 왼쪽 오른쪽 아래 위 아랫층 윗층
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(queue):
    global day
    while queue:
        node = queue.popleft()
        h, n, m = node[0], node[1], node[2]
        for i in range(6):
            z, y, x = h + dz[i], n + dy[i], m + dx[i]
            if 0<=x<M and 0<=y<N and 0<=z<H and graph[z][y][x] == 0:
                graph[z][y][x] = graph[h][n][m] + 1
                queue.append([z, y, x])
                day = graph[z][y][x]

M, N, H = map(int, input().split())
graph = [[[0 for _ in range(M)] for __ in range(N)] for ___ in range(H)]
queue = collections.deque()
isTrue = True
day = 1
for h in range(H):
    for n in range(N):
        graph[h][n] = list(map(int, input().split()))

for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 1:
                queue.append([h,n,m])

bfs(queue)

for h in range(H):
    if isTrue:
        for n in range(N):
            if isTrue:
                for m in range(M):
                    if graph[h][n][m] == 0:
                        isTrue = False
if isTrue:
    print(day - 1)
else:
    print('-1')