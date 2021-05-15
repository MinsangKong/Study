#https://www.acmicpc.net/problem/17298
#백준 17298번 오큰수(DP)
#import sys
#input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [-1] * n
check = []

for i in range(n-1,-1,-1):
    num = nums[i]
    while check and check[-1] <= num:
        check.pop()
    if check:
        dp[i] = check[-1]
    check.append(num)
    
print(*dp)
        