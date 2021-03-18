import sys

N = int(input())
stack = list(map(int, input().split()))

result = []
while stack:
    node = stack.pop()
    if not stack:
        result.append(0)
        break
    check = 0
    for i in range(len(stack) - 1, -1, -1):
        if node <= stack[i]:
            result.append(i + 1)
            check = 1
            break
    if check == 0:
        result.append(0)
result.reverse()
print(*result)

#최적화 필요