import sys
input = sys.stdin.readline

def apchuk(si, sj, d, result):

    color = graph[si][sj]
    isTrue = True
    for i in range(si, si + d):
        for j in range(sj, sj + d):
            if graph[i][j] != color:
                isTrue = False
    if not isTrue:
        # result.append('(')
        d = d // 2
        apchuk(si, sj, d, result)
        apchuk(si + d, sj, d, result)
        apchuk(si, sj + d, d, result)
        apchuk(si + d, sj + d, d, result)
    else:
        result.append(str(color))
        # result.append(')')
        return


N = int(input())
graph = []
result = []
for i in range(N):
    graph.append(list(map(int, list(input().strip()))))
apchuk(0, 0, N, result)
print(*result)
# for i in range(N):
#     print(graph[i])


