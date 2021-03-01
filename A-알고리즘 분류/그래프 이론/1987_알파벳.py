import sys
import collections
input = sys.stdin.readline

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(cur_i, cur_j):
    global max_ans
    queue = set()
    queue.add(((cur_i, cur_j), (graph[0][0])))
    while queue:
        node, visited = queue.pop()
        # print(node, visited)
        ci, cj = node[0], node[1]
        for i in range(4):
            ni, nj = ci + di[i], cj + dj[i]
            if 0 <= ni < R and 0 <= nj < C:
                if graph[ni][nj] not in visited:
                    queue.add(((ni, nj), visited + graph[ni][nj]))
                    max_ans = max(max_ans, len(visited) + 1)
    return max_ans

R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(map(str, input().strip())))
max_ans = 1
print(bfs(0, 0))
