import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    arr = list(input().strip())
    stack = []
    flag = 0
    while arr:
        x = arr.pop()
        if x == ')':
            stack.append(x)
        else:
            if stack:
                stack.pop()
            else:
                flag = 1
    if flag == 1 or stack:
        print("NO")
    else:
        print("YES")