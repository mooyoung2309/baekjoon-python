import sys
import collections
input = sys.stdin.readline

def bfs(graph: list, root: list):
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        i = node[0]
        j = node[1]
        if graph[i][j] == 1:
            graph[i][j] = 0
            if i > 0:
                queue.append([i - 1,j])
            if j > 0:
                queue.append([i, j - 1])
            if i + 1 < len(graph):
                queue.append([i + 1, j])
            if j + 1 < len(graph[i]):
                queue.append([i, j + 1])

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    baechu = [[0 for _ in range(M)] for __ in range(N)]
    for __ in range(K):
        j, i = map(int, input().split())
        baechu[i][j] = 1
    count = 0
    for i in range(N):
        for j in range(M):
            if baechu[i][j] == 1:
                bfs(baechu, [i, j])
                count += 1
    print(count)