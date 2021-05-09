#https://www.acmicpc.net/problem/11722
#백준 11722번 가장 긴 감소하는 부분 수열(DP)
#import sys
#input = sys.stdin.readline
import bisect

n = int(input())
nums = list(map(int, input().split()))

if n == 1 :
    print(1)
else:
    check = [nums[-1]]
    for i in range(n-2, -1,-1):
        if check[-1] < nums[i]:
            check.append(nums[i])
        else:
            check[bisect.bisect_left(check,nums[i])] = nums[i]
            
    print(len(check))
    