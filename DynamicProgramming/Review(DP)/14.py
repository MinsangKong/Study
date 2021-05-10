#https://www.acmicpc.net/problem/14003
#백준 14003번 가장 긴 증가하는 부분 수열5(dp)
#import sys
#input = sys.stdin.readline
import bisect

n = int(input())
nums = list(map(int, input().split()))
dp = [0] * n #부분 수열의 길이 값
check = [nums[0]] #부분수열의 값
for i in range(1,n):
    if check[-1] < nums[i]:
        check.append(nums[i])
        dp[i] = len(check)-1
    else:
        dp[i] = bisect.bisect_left(check, nums[i])
        check[dp[i]] = nums[i]

length = len(check)-1
result = []
print(length+1)
for i in range(n-1,-1,-1):
    if dp[i] == length:
        result.append(nums[i])
        length-=1
print(*dp)    
print(*result[::-1])