#https://www.acmicpc.net/problem/19566
#백준 19566번 수열의 구간 평균(누적합)
import sys
input = sys.stdin.readline
from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(int, input().split()))

result = 0
subSum = 0
subList = defaultdict(int)

for i in range(n):
    subSum+=nums[i]
    point = subSum-(i+1)*k
    
    result += subList[point]
    subList[point]+=1
    
print(result+subList[0])