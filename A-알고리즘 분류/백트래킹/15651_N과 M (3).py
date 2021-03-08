import sys
input = sys.stdin.readline

def backtracking(result,n):
    if result and len(result) >= M:
        print(*result)
        return
    else:
        for i in range(n, N+1):
            tmp = []
            tmp.extend(result)
            tmp.append(i)
            backtracking(tmp,i)

N, M = map(int, input().split())
backtracking([],1)