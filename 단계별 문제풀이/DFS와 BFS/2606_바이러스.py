import sys
import collections
input = sys.stdin.readline

num_computer = int(input())
num_network = int(input())
graph = collections.defaultdict(list)

for _ in range(num_network):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(root: int):
    visited = []
    dq = collections.deque([root])

    while dq:
        n = dq.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                dq.extend(graph[n])
    return visited

print(len(bfs(1)) - 1)