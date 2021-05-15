#https://www.acmicpc.net/problem/14465
#백준 14465번 소가 길을 건너간 이유5(이분탐색,DP)
#import sys
#input = sys.stdin.readline
from itertools import combinations

n, k, b = map(int, input().split())
light = [1]*n
check = []
for _ in range(b):
    num = int(input())
    light[num-1] = 0
    
result = b
cnt = 0
for i in range(k):
    if light[i] == 0:
        cnt+=1
        
if k == n:
    print(cnt)
else:
    for i in range(k,n):
        if light[i] == 0:
            cnt+=1
        if light[i-k] == 0:
            cnt-=1
        if result > cnt:
            result = cnt
    print(result)
    
'''
combinations 함수를 사용하면 시간초과가 발생한다. 그래서 누적합을 활용해서 문제 해결
'''