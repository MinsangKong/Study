import sys
from bisect import bisect_left
input = sys.stdin.readline


m, n, l = map(int, input().split())
base = list(map(int, input().split()))
base.sort()

ans = 0

for _ in range(n):
    x, y = map(int, input().split())
    idx = bisect_left(base, x)

    if idx == 0:
        if abs(x-base[idx]) + y <= l:
            ans += 1
    elif idx == m:
        if abs(x-base[idx-1]) + y <= l:
            ans += 1
    else:
        if abs(x-base[idx]) + y <= l or abs(x-base[idx-1]) + y <= l:
            ans += 1

print(ans)
'''
가장 이해가 가는 풀이법. 같은 값이면 가장 왼쪽 값을 반환하는 bisect_left 함수를
활용해서 경우의 수에 맞추어 횟수를 카운트했다.
'''