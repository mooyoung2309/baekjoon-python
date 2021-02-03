import heapq
import collections
V, E = map(int, input().split())
target = int(input())
graph = collections.defaultdict(dict)
for _ in range(E):
    u, v, w = map(int, input().split())
    dic = {}
    dic[v] = w
    graph[u][v] = w
print(graph)

def dijkstra(graph, first):
    distance = {node:[100, first] for node in graph}
    distance[first] = [0,1]
    queue = []
    heapq.heappush(queue, [distance[first], first])

    while queue:
        print(queue)
        c_distance, c_node = heapq.heappop(queue)

        if distance[c_node][0] < c_distance:
            continue
        for adj, weight in graph[c_node].items():
            t_distance = c_distance + weight

            if(t_distance < distance[adj][0]):
                distance[adj] = [adj, t_distance]
                heapq.heappush(queue, [t_distance, adj])

    return distance

print(dijkstra(graph, target))