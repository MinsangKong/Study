#https://www.acmicpc.net/problem/2015
#백준 2015번 수들의 합 4(누적합)
#import sys
#input = sys.stdin.readline
from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(int, input().split()))

book = defaultdict(int)
result = 0
book[nums[0]] = 1

for i in range(1, n):
    nums[i] += nums[i-1]
    
    result += book[nums[i]-k]
    book[nums[i]]+=1
    
print(result+book[k])