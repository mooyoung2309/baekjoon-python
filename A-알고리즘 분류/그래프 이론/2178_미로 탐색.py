import sys
import collections
input = sys.stdin.readline

def bfs(root, graph):
    queue = collections.deque([root])
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        node = queue.popleft()
        a, b = node[0], node[1]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M and graph[x][y] == '1':
                queue.append([x, y])
                graph[x][y] = graph[a][b] + 1

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(str(input().strip())))
graph[0][0] = 1
bfs([0,0], graph)
print(graph[N-1][M-1])


