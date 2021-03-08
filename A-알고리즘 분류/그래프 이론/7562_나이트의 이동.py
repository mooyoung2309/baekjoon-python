import sys
import collections

input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs(cur, des, dp):
    queue = collections.deque([cur])
    dp[cur[0]][cur[1]] = 0
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        if [x, y] == des:
            return dp[x][y]
        for i in range(8):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < I and 0 <= b < I and dp[a][b] == -1:
                dp[a][b] = dp[x][y] + 1
                queue.append([a, b])


T = int(input())
for _ in range(T):
    I = int(input())
    cur_x, cur_y = map(int, input().split())
    des_x, des_y = map(int, input().split())
    dp = [[-1 for _ in range(I)] for __ in range(I)]
    print(bfs([cur_x, cur_y], [des_x, des_y], dp))
