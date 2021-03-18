import sys
import collections
input = sys.stdin.readline

N = int(input())
queue = collections.deque()
for i in range(1, N + 1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    a = queue.popleft()
    queue.append(a)

print(*queue)
