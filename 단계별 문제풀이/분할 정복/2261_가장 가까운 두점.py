import sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))

distances = []
for i in range(0, N):
    for j in range(i+1, N):
        x = nums[i][0] - nums[j][0]
        y = nums[i][1] - nums[j][1]
        distances.append(x*x+y*y)
print(min(distances))
