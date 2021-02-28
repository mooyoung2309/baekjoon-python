import sys
import collections
import heapq
input = sys.stdin.readline

def dijkstra(start, graph, n):
    distance = [sys.maxsize for _ in range(n + 1)]
    distance[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if distance[current_node] < current_distance:
            continue
        for d, n in graph[current_node]:
            next_distance = d + current_distance
            if next_distance < distance[n]:
                distance[n] = next_distance
                heapq.heappush(heap, [next_distance, n])
    return distance

T = int(input())
for _ in range(T):
    n, m ,t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = collections.defaultdict(list)
    for __ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([d, b])
        graph[b].append([d, a])
    s_d = dijkstra(s, graph, n)
    g_d = dijkstra(g, graph, n)
    h_d = dijkstra(h, graph, n)
    result = []
    for __ in range(t):
        x = int(input())
        if s_d[x] == s_d[g] + g_d[h] + h_d[x] or s_d[x] == s_d[h] + h_d[g] + g_d[x]:
            result.append(x)
    print(*sorted(result))