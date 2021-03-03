import sys
import heapq

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    deadline, cupNoodle = map(int, input().split())
    arr.append((deadline, cupNoodle))

arr.sort(key = lambda x : (x[0], -x[1]))

heap = []
for val in arr:
    heapq.heappush(heap, val[1])
    if val[0] < len(heap):
        heapq.heappop(heap)

print(sum(heap))