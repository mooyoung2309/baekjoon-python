import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jews = []
for _ in range(N):
    M, V = map(int, input().split())
    heapq.heappush(jews, [M, V])
bags = []
for _ in range(K):
    C = int(input())
    bags.append(C)

bags.sort()

answer = 0
tmp_jew = []
for bag in bags:
    while jews and bag >= jews[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jews)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not jews:
        break
print(answer)
