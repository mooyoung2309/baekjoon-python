import sys

def bfs():
    stack = []
    stack.append()
    while stack:
        node = stack.pop()


def searchBf():

    return 0

N, M = map(int, input().split())
graph_map = []
for _ in range(N):
    graph_map.append(list(map(int, input().split())))

#빈 칸의 인덱스 저장
arr_empty = []
for i in range(len(graph_map)):
    for j in range(len(graph_map[0])):
        if graph_map[i][j] == 0:
            arr_empty.append((i, j))



for i in range(N):
    print(graph_map[i])

#모든 경우를 다 찾아서 BFS로 바이러스 맵 완성 그 후 카운트 -> 최댓값 알아내기