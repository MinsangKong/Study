#https://www.acmicpc.net/problem/2156
#백준 2156번 포도주 시식(DP)
#import sys
#input = sys.stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]

if n == 1:
    print(wines[0])
elif n == 2 :
    print(wines[0]+wines[1])
else:
    dp = [0]*n
    dp[0] = wines[0]
    dp[1] = wines[0]+wines[1]
    dp[2] = max(dp[0]+wines[2], dp[1],wines[1]+wines[2])
    for i in range(3,n):
        dp[i] = max(dp[i-1], dp[i-2]+wines[i], dp[i-3]+wines[i]+wines[i-1])
    print(dp[n-1])