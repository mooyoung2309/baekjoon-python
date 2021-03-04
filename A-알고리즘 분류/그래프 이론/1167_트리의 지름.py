import sys
import collections
import copy

def bfs(queue):
    global max_sum

    while queue:
        node, visited, sum = queue.popleft()
        for val in graph[node]:
            if visited[val[0]]:
                visited_tmp = copy.deepcopy(visited)
                visited_tmp[val[0]] = False
                queue.append((val[0], visited_tmp, sum + val[1]))
                max_sum = max(max_sum, sum + val[1])

V = int(input())
graph = collections.defaultdict(list)
queue = collections.deque()
for i in range(1, V + 1):
    tmp = list(map(int, input().split()))
    cnt = 0
    for j in range(1, len(tmp) -1, 2):
        graph[i].append((tmp[j], tmp[j+1]))
        cnt += 1
    if cnt <= 1:
        visited_tmp = [True] * (V+1)
        visited_tmp[i] = False
        queue.append((i, visited_tmp, 0))

max_sum = 0

bfs(queue)
print(max_sum)
