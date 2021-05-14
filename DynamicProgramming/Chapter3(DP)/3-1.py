#Q33 퇴사
#https://www.acmicpc.net/problem/14501
#백준 14501번 퇴사(DP)
#import sys
#input = sys.stdin.readline

n = int(input())
info = []

for _ in range(n):
    info.append(list(map(int, input().split())))
    
dp = [0]*(n+1)

for i in range(n):
    day, cost = info[i][0], info[i][1]
    dp[i] = max(dp[:i+1])
    if i+day <= n:
        dp[i+day]=max(dp[i+day], dp[i]+cost)
print(dp)