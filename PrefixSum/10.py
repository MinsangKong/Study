#https://www.acmicpc.net/problem/11659
#백준 11659번 구간 합 구하기 4 (누적합)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [0]+list(map(int, input().split()))
dp = [0]*(n+1)

dp[1] = nums[1]

for i in range(2,n+1):
    dp[i] = dp[i-1]+nums[i]
    
for _ in range(m):
    a,b = map(int, input().split())
    if a > b:
        print(dp[a]-dp[b-1])
    else :
        print(dp[b]-dp[a-1])