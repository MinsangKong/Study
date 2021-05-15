#https://www.acmicpc.net/problem/12015
#백준 12015번 가잔 긴 증가하는 부분 수열2(DP)
#import sys
#input = sys.stdin.readline
import bisect

n = int(input())
nums = list(map(int, input().split()))

dp = [nums[0]]
for i in range(1, n):
    if dp[-1] < nums[i]:
        dp.append(nums[i])
    else:
        dp[bisect.bisect_left(dp,nums[i])] = nums[i]
        
print(len(dp))