import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    heap.append(x)
    heap.sort()

    if len(heap) % 2 == 0:
        print(min(heap[len(heap) // 2 - 1], heap[len(heap) // 2]))
    else:
        print(heap[len(heap) // 2])