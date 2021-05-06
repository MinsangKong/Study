#https://www.acmicpc.net/problem/2193
#백준 2193번 이친수(DP)
#import sys
#input = sys.stdin.readline

n = int(input().rstrip())

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    result = [0]*(n+1)
    result[1] = 1
    result[2] = 1
    for i in range(3,n+1):
        result[i] = result[i-1]+result[i-2]
        
    print(result[n])