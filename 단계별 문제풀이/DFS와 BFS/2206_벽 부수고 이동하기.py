import sys
import collections

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def bfs(start, end, graph, dp):
    queue = collections.deque([start])
    dp[start[0]][start[1]] = 1
    while queue:
        node = queue.popleft()
        x = node[0]
        y = node[1]
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < N and 0 <= b < M:
                if graph[x][y] == '1' and graph[a][b] == '1':
                    break
                if dp[a][b] == -1:
                    dp[a][b] = dp[x][y] + 1
                    queue.append([a, b])
        for i in range(len(dp)):
            print(dp[i])
        print()

N, M = map(int, input().split())
graph = []
dp = [[-1 for _ in range(M)] for __ in range(N)]
for _ in range(N):
    graph.append(list(str(input().strip())))
bfs([0, 0], [N - 1, M - 1], graph, dp)
print(dp[N - 1][M - 1])
