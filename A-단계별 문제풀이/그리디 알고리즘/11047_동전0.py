N, K = map(int, input().split())
dongjun = []
for _ in range(N):
    dongjun.append(int(input()))
dongjun = reversed(dongjun)

count = 0
for i in dongjun:
    count += K//i
    K = K%i

print(count)