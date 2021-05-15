#https://www.acmicpc.net/problem/8394
#백준 8394번 악수(DP)
#import sys
#input = sys.stdin.readline

n = int(input())
if n == 1 :
    print(1)
elif n == 2:
    print(2)
else:
    result = [0]*(n+1)
    result[1] = 1
    result[2] = 2
    for i in range(3,n+1):
        result[i] = (result[i-2]+result[i-1])%10
        
    print(result[n])
'''
문제에 포인트는 동시에 악수는 불가능하다는 점이다. 헷갈려서 그 부분에서 계속 틀렸다.
'''