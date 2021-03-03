import math
import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))

print(math.factorial(N)//(math.factorial(K) * math.factorial(N-K)))