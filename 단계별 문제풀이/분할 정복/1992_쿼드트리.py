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
        result.append('(')
        d = d // 2
        apchuk(si, sj, d, result)
        apchuk(si, sj + d, d, result)
        apchuk(si + d, sj, d, result)
        apchuk(si + d, sj + d, d, result)
        result.append(')')
    else:
        result.append(str(color))
        return


N = int(input())
graph = []
result = []
for i in range(N):
    graph.append(list(map(int, list(input().strip()))))
apchuk(0, 0, N, result)

for i in range(len(result)):
    print(result[i], end = "")