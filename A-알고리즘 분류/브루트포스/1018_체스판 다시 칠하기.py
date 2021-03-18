import sys

input = sys.stdin.readline

def bruteforce(si, sj):
    cnt1 = 0
    cnt2 = 0
    #짝수일때 B 홀수일때 W가 정상적임
    for i in range(si, si + 8):
        for j in range(sj, sj + 8):
            if (i + j - si - sj) % 2 == 0 and graph[i][j] != 'B':
                cnt1 += 1
            else:
                cnt2 += 1
            if (i + j - si - sj) % 2 == 1 and graph[i][j] != 'W':
                cnt1 += 1
            else:
                cnt2 += 1
    print(cnt1, cnt2)
    return min(cnt1, cnt2)


N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(str, input().strip())))

min_cnt = sys.maxsize
for i in range(0, N - 7):
    for j in range(0, M - 7):
        min_cnt = min(bruteforce(i, j), min_cnt)
print(min_cnt)