import sys
input = sys.stdin.readline

N = int(input())

graph = [[0 for _ in range(3)] for __ in range(N)]
dp = [[0 for _ in range(3)] for __ in range(N)]
dp = [[0 for _ in range(3)] for __ in range(N)]
max_paint = []
for i in range(N):
    graph[i] = list(map(int, input().split()))


for k in range(3):
    dp[0][0] = sys.maxsize
    dp[0][1] = sys.maxsize
    dp[0][2] = sys.maxsize
    dp[0][k] = graph[0][k]
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + graph[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + graph[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + graph[i][2]
        if i == N - 1:
            dp[i][k] = sys.maxsize
            max_paint.append(min(dp[i]))

print(min(max_paint))