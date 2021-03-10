import sys
import collections

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    indegree = [0 for _ in range(N + 1)]
    dp = [0 for _ in range(N + 1)]
    for __ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1


    queue = collections.deque()
    # 진입 차수 0 -> 큐 삽입
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = times[i]

    while queue:
        node = queue.popleft()

        for i in graph[node]:#노드의 연결된 다음 노드들을 탐색한다.
            indegree[i] -= 1 #탐색을 했다는건 진입차수가 줄었다는 것
            dp[i] = max(dp[node] + times[i], dp[i]) #DP는 기존까지 계산한 시간 or 이전 노드의 계산한 시간 + 자신 노드 시간
            if indegree[i] == 0:#진입차수가 0이되면면
               queue.append(i)
    W = int(input())
    print(dp[W])