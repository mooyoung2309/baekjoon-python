import sys
input = sys.stdin.readline

N = int(input())
jongee = []
white = 0
blue = 0
for _ in range(N):
    jongee.append(list(map(int, input().split())))

def check(si: int, sj: int, d: int):
    cnt = 0
    global blue, white
    for i in range(si, si + d):
        for j in range(sj, sj + d):
            if jongee[i][j] == 1:
                cnt += 1
    if cnt == 0:
        white += 1
        return
    if cnt == d*d:
        blue += 1
        return
    else:
        d = d//2
        check(si, sj, d)
        check(si + d, sj, d)
        check(si, sj +d, d)
        check(si + d, sj + d, d)

check(0,0, N)
print(white)
print(blue)
