import sys
input = sys.stdin.readline


def go(red, blue, graph, type) -> list:
    return [0]


N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(str, input().strip())))
for i in range(len(graph)):
    print(graph[i])