import sys
import collections

input = sys.stdin.readline


def bfs(root):
    queue = collections.deque([root])
    value[root] = 1

    while queue:
        node = queue.popleft()
        for v in graph[node]:
            if value[v] == 0:
                queue.append(v)
                value[v] = value[node] * -1
            elif value[v] == value[node]:
                return False
    return True


T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    graph = collections.defaultdict(list)
    value = [0 for _ in range(V + 1)]
    istrue = True
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    for i in range(1, V + 1):
        if value[i] == 0:
            if not bfs(i):
                istrue = False
                break
    print('YES' if istrue else 'NO')
