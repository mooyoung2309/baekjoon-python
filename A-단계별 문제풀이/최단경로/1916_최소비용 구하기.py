import sys
import collections
import heapq

input = sys.stdin.readline

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(heap, (distance[start], start))

    while heap:
        current_dis, current_node = heapq.heappop(heap)
        if distance[current_node] < current_dis:
            continue
        for d, n in graph[current_node]:
            next_dis = d + distance[current_node]
            if next_dis < distance[n]:
                distance[n] = next_dis
                heapq.heappush(heap, (distance[n], n))

N = int(input())
M = int(input())
graph = collections.defaultdict(list)
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))
sp, ep = map(int, input().split())
distance = [sys.maxsize for _ in range(N + 1)]
heap = []
dijkstra(sp)
print(distance[ep])