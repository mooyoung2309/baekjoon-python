import sys
import collections
import heapq

input = sys.stdin.readline


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance = [sys.maxsize for _ in range(V + 1)]
    distance[start] = 0

    while heap:
        cur_dis, cur_node = heapq.heappop(heap)
        if distance[cur_node] < cur_dis:
            continue
        for n, d in graph[cur_node]:
            next_dis = d + cur_dis
            if next_dis < distance[n]:
                distance[n] = next_dis
                heapq.heappush(heap, (next_dis, n))

    return distance


V = int(input())
graph = collections.defaultdict(list)

for i in range(1, V + 1):
    tmp = list(map(int, input().split()))
    for j in range(1, len(tmp), 2):
        if tmp[j] == -1:
            break
        graph[tmp[0]].append((tmp[j], tmp[j + 1]))

dis1 = dijkstra(1)
max_v1 = dis1.index(max(dis1[1:]))
dis2 = dijkstra(max_v1)
max_dis2 = max(dis2[1:])
print(max_dis2)
