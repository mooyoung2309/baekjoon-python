import sys
import collections
import heapq

input = sys.stdin.readline


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance = [sys.maxsize for _ in range(N + 1)]
    distance[start] = 0

    while heap:
        cur_distance, cur_node = heapq.heappop(heap)
        if distance[cur_node] < cur_distance:
            continue
        for d, n in graph[cur_node]:
            next_dis = d + cur_distance
            if next_dis < distance[n]:
                distance[n] = next_dis
                heapq.heappush(heap, (next_dis, n))
    return distance


N = int(input())
graph = collections.defaultdict(list)
for _ in range(N - 1):
    U, V, W = map(int, input().split())
    graph[U].append((W, V))
    graph[V].append((W, U))

distance1 = dijkstra(1)

max_node1 = distance1.index(max(distance1[1:]))
distance2 = dijkstra(max_node1)
max_distance = max(distance2[1:])

print(max_distance)
