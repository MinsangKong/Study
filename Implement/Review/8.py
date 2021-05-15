#https://www.acmicpc.net/problem/10773
#백준 10773번 제로(구현)
#import sys
#input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    cost = int(input())
    if cost == 0:
        arr.pop()
        continue
    arr.append(cost)
    
print(sum(arr))
    