#https://www.acmicpc.net/problem/10986
#백준 10986번 나머지 합 (누적합)
#import sys
#input = sys.stdin.readline
from collections import defaultdict

n, m = map(int, input().split())
nums = list(map(int, input().split()))

book = defaultdict(int)

total = 0
cnt = 0

for i in range(n):
    total += nums[i]
    target = total% m
    
    cnt += book[target]
    book[target] += 1
    
print(cnt+book[0])