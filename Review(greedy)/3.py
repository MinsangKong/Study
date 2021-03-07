#https://www.acmicpc.net/problem/13417
#백준 13417번 카드 문자열(그리디)
from collections import deque

t = int(input())
for i in range(t):
    n = int(input())
    alp = input().split()
    result = deque()
    result.append(alp.pop(0))
    for j in alp:
        if ord(result[0]) >= ord(j):
            result.appendleft(j)
        else:
            result.append(j)
    print(''.join(result))
            