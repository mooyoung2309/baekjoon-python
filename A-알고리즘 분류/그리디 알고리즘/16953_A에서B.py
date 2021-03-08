import sys
import collections

input = sys.stdin.readline

A, B = map(int, input().split())
queue = collections.deque([(B, 1)])
result = -1

while queue:
    x, cnt = queue.popleft()
    if x == A:
        result = cnt
        break
    if x % 2 == 0 and x / 2 >= A:
        queue.append((x / 2, cnt + 1))
    elif x % 10 == 1 and x // 10 >= A:
        queue.append((x // 10, cnt + 1))
    else:
        break
print(result)
