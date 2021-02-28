import heapq
import sys

N = int(sys.stdin.readline().rstrip())
max_heap = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if not max_heap:
            print(0)
        else:
            print(heapq.heappop(max_heap)[1])
    else:
        heapq.heappush(max_heap, (-x, x))