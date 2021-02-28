import sys
input = sys.stdin.readline

K = int(input())
stack = []
for _ in range(K):
    a = int(input())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

print(sum(stack))