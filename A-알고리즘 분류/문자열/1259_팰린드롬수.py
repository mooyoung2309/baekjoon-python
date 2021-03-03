import sys
import copy
input = sys.stdin.readline

while True:
    x = list(input().strip())

    if x == ['0']:
        break
    y = copy.deepcopy(x)
    y.reverse()

    if x == y:
        print('yes')
    else:
        print('no')