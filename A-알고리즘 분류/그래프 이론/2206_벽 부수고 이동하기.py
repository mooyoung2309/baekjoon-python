import sys
import collections

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def bfs(graph):
    queue = collections.deque()
    queue.append([0,0,1])
    dp = [[[0] * 2 for i in range(M)] for i in range(N)]
    dp[0][0][1] = 1
    while queue:
        x, y, w = queue.popleft()
        if x == N - 1 and y == M - 1:
            return dp[x][y][w]
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < N and 0 <= b < M:
                if graph[a][b] == 1 and w == 1:
                    dp[a][b][0] = dp[x][y][1] + 1
                    queue.append([a, b, 0])
                elif graph[a][b] == 0 and dp[a][b][w] == 0:
                    dp[a][b][w] = dp[x][y][w] + 1
                    queue.append([a, b, w])
    return -1

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input().strip()))))

print(bfs(graph))
