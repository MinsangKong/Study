#https://www.acmicpc.net/problem/21757
#백준 21757번 나누기(누적합)
#import sys
#input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

prefixSum = [0]*n
prefixSum[0] = nums[0]

for i in range(1,n):
    prefixSum[i] = prefixSum[i-1]+nums[i]
    
if prefixSum[n-1]%4 != 0:
    print(0)
else:
    dp = [0]*4
    dp[0] = 1
    base = prefixSum[n-1]//4
    for i in range(n-1):
        if prefixSum[i] == base*3:
            dp[3] += dp[2]
        if prefixSum[i] == base*2:
            dp[2] += dp[1]
        if prefixSum[i] == base:
            dp[1] += dp[0]
    print(dp[3])