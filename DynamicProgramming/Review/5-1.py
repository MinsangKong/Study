#https://www.acmicpc.net/problem/9656
#백준 9656번 돌 게임2(DP)
#import sys
#input = sys.stdin.readline

n = int(input())
if n == 1 or n == 3:
    print("CY")
elif n == 2:
    print("SK")
else:
    result = [0] * (n+1)
    result[1] = 1
    result[2] = 0
    result[3] = 1
    
    for i in range(4,n+1):
        if i%2 == 0:
            if result[i-1] == 1 or result[i-3] == 1:
                result[i] = 0
        else:
            if result[i-1] == 0 or result[i-3] == 0:
                result[i] = 1
                
    if result[n] == 0:
        print("SK")
    else:
        print("CY")
'''
무조건 DP를 구현해야 한다고 생각해서 더 비효율적으로 계산했다.
'''