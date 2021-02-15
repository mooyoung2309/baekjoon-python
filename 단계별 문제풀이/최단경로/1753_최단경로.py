import sys
import heapq
import collections

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
graph = collections.defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

distance = [sys.maxsize]*(V+1)
heap = []
print(graph)
def dijkstra(start):
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        print(heap)
        current_distance, current_node = heapq.heappop(heap)
        if distance[current_node] < current_distance:
            continue
        for d, n in graph[current_node]:
            next_distance = d + current_distance
            if next_distance < distance[n]:
                distance[n] = next_distance
                heapq.heappush(heap, (next_distance, n))

dijkstra(K)
for i in range(1, V+1):
    print("INF" if distance[i] == sys.maxsize else distance[i])