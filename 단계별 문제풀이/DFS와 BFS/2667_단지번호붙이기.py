import sys

input = sys.stdin.readline

N = int(input())
danji = [[0]*N for _ in range(N)]
stack = []
for i in range(N):
    danji[i] = list(str(input().strip()))
    for j in range(N):
        if danji[i][j] == '1':
            stack.append([i,j])

result = []
def dfs(root):
    stack = [root]
    count = 0

    while stack:
        node = stack.pop()
        i, j = node[0], node[1]
        if danji[i][j] == '1':
            danji[i][j] = '0'
            count += 1
            if i > 0:
                stack.append([i - 1, j])
            if j > 0:
                stack.append([i, j-1])
            if i < N - 1:
                stack.append([i + 1, j])
            if j < N - 1:
                stack.append([i, j + 1])
    result.append(count)

for i in range(N):
    for j in range(N):
        if danji[i][j] == '1':
            dfs([i,j])
result.sort()
print(len(result))
print(*result, sep='\n')