import sys
import collections

input = sys.stdin.readline


def bfs(start, end):
    queue = collections.deque()
    queue.append(start)

    while queue:
        x = queue.popleft()
        if x == end:
            return dp[x]

        if 0 <= x + 1 < 100001 and dp[x + 1] == 0:
            queue.append(x + 1)
            dp[x + 1] = dp[x] + 1
        if 0 <= x - 1 < 100001 and dp[x - 1] == 0:
            queue.append(x - 1)
            dp[x - 1] = dp[x] + 1
        if 0 <= x * 2 < 100001 and dp[x * 2] == 0:
            queue.append(x * 2)
            dp[x * 2] = dp[x] + 1


N, K = map(int, input().split())
dp = [0 for _ in range(100001)]
print(bfs(N, K))