import sys
import collections
input = sys.stdin.readline

def bfs(graph, queue):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    global count
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if 0 <= a < N and 0 <= b < M and (graph[a][b] == 0):
                graph[a][b] = graph[x][y] + 1
                queue.append([a, b])
                count = graph[x][y]

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
count = 0
queue = collections.deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i,j])
bfs(graph, queue)

check = True
for row in graph:
    if 0 in row:
        check = False
        break

if check:
    print(count)
else:
    print(-1)
