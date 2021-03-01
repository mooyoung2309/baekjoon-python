import heapq
import sys

input = sys.stdin.readline

N = int(input())

time = [list(map(int,input().split())) for _ in range(N)]
time.sort(key=lambda x: (x[0], x[1]))

queue = []
heapq.heappush(queue,time[0][1])

for i in range(1,N):
    if queue[0] > time[i][0]:
        heapq.heappush(queue,time[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue,time[i][1])

print(len(queue))