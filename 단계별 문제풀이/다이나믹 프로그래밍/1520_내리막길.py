import sys
import collections

input = sys.stdin.readline
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def dfs(start):
    stack = []
    stack.append(start)
    dp[0][0] = 1
    while stack:
        node = stack.pop()
        ci, cj = node[0], node[1]
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < M and 0 <= nj < N and graph[ni][nj] < graph[ci][cj]:
                dp[ni][nj] += dp[ci][cj]
                stack.append([ni, nj])
        for i in range(len(dp)):
            print(dp[i])
        print(" ")


M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[0 for _ in range(N)] for __ in range(M)]
dfs([0,0])