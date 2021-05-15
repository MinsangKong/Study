#https://www.acmicpc.net/problem/16112
#백준 16112번 5차 전직(정렬)
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())
stone = list(map(int, input().split()))
result = 0
stone.sort()
for i in range(n):
    if i < k:
        result+=stone[i]*i
    else:
        result+=stone[i]*k
print(result)    