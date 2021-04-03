#https://www.acmicpc.net/problem/19621
#백준 19621번 회의실 배정 2(DP)
import sys
input = sys.stdin.readline

N = int(input())
booked = []

for _ in range(N):
    booked.append(list(map(int, input().split())))

dp = [0] * N
dp[0] = booked[0][2]
res = dp[0]
if N > 1:
    dp[1] = booked[1][2]
    res = max(dp[0], dp[1])

for i in range(1, N):
    for j in range(0, i - 1):
        dp[i] = max(dp[i], dp[j] + booked[i][2])
    res = max(res, dp[i])

print(res)
'''
다른 사람이 푼 방식을 보니까 dfs를 적용하지 않고 dp적인 사고로 문제를 풀었는데
시간적인 측면에서 dfs보다 훨씬 빨랐다.
'''