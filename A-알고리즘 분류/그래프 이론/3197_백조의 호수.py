import sys
import collections
import copy
input = sys.stdin.readline

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def swanDfs():
    queue = collections.deque()
    queue.append(swan[0])
    graph_tmp = copy.deepcopy(graph)

    while queue:
        node = queue.popleft()
        ci, cj = node[0], node[1]
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            #갈 수 있는 물을 만난다면
            if 0 <= ni < R and 0 <= nj < C:
                if (ni, nj) == swan[1]:
                    return True
                if graph_tmp[ni][nj] == '.':
                    graph_tmp[ni][nj] = 'V'
                    queue.append((ni, nj))
    return False

def bfs():
    day = 0

    while queue:
        node = queue.popleft()
        ci, cj = node[0], node[1]
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < R and 0 <= nj < C and graph[ni][nj] == 'X':
                graph[ni][nj] = '.'
                dp[ni][nj] = dp[ci][cj] + 1
                day = dp[ni][nj]
                queue.append((ni, nj))
        if swanDfs():
            print(day)
            return

R, C = map(int, input().split())
dp = [[0 for _ in range(C)] for __ in range(R)]
graph = []
for _ in range(R):
    graph.append(list(map(str, input().strip())))

queue = collections.deque()
swan = []
for i in range(R):
    for j in range(C):
        if graph[i][j] == '.':
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < R and 0 <= nj < C and graph[ni][nj] == 'X':
                    queue.append((i, j))
                    break
        elif graph[i][j] == 'L':
            swan.append((i,j))
bfs()
