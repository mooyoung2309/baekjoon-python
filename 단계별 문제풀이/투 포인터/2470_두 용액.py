import sys
input = sys.stdin.readline

N = int(input())
yongaeks = list(map(int, input().split()))
yongaeks.sort()

sp = 0
ep = len(yongaeks) - 1
sum_yongaeks = []
indx = -1
while sp < ep:
    indx += 1
    sum = yongaeks[sp] + yongaeks[ep]
    tmp = [yongaeks[sp],yongaeks[ep],abs(sum)]
    sum_yongaeks.append(tmp)
    if sum > 0:
        ep -= 1
    elif sum < 0:
        sp += 1
    else:
        break

sum_yongaeks.sort(key= lambda x : x[2])
print(sum_yongaeks[0][0], sum_yongaeks[0][1])