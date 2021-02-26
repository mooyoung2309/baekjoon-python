import sys
import collections
import heapq

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dijkstra(start):
    distance[start[0]][start[1]] = 0
    heapq.heappush(heap, (distance[start[0]][start[1]], start))

    while heap:
        current_dis, current_node = heapq.heappop(heap)
        if distance[current_node[0]][current_node[1]] < current_dis:
            continue
        for i in range(4):
            next_node = [0] * 2
            next_node[0] = current_node[0] + dx[i]
            next_node[1] = current_node[1] + dy[i]
            if 0 <= next_node[0] < N and 0 <= next_node[1] < M:
                next_distance = distance[current_node[0]][current_node[1]] + (1 if graph[next_node[0]][next_node[1]] == 1 else 0)
                if next_distance < distance[next_node[0]][next_node[1]]:
                    distance[next_node[0]][next_node[1]] = next_distance
                    heapq.heappush(heap, (distance[next_node[0]][next_node[1]], next_node))

M, N = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, list(input().strip()))))
distance = [[sys.maxsize for _ in range(M)] for __ in range(N)]
heap = []
dijkstra([0,0])
print(distance[N-1][M-1])