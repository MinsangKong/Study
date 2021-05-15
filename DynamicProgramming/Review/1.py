#https://www.acmicpc.net/problem/2493
#백준 2493번 탑(백준, 그리디)
#import sys
#input = sys.stdin.readline
import bisect

n = int(input())
signals = list(map(int, input().split()))

dp = [0]*n
check = []

for i in range(n):
    signal = signals[i]
    while check and signals[check[-1]] < signal:
        check.pop()
    if check:
        dp[i] =check[-1]+1
    check.append(i)
    
print(*dp)