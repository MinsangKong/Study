#https://www.acmicpc.net/problem/15990
#백준 15990번 1,2,3 더하기 5(DP)
#import sys
#input = sys.stdin.readline
result = [[0]*3 for i in range(100001)]
    
result[1][0] = 1
result[2][1] = 1
result[3][0] = 1
result[3][1] = 1
result[3][2] = 1

for i in range(4,100001):
    result[i][0] = (result[i-1][1]+result[i-1][2])%1000000009
    result[i][1] = (result[i-2][0]+result[i-2][2])%1000000009
    result[i][2] = (result[i-3][0]+result[i-3][1])%1000000009
t = int(input())
for i in range(t):
    n = int(input())
    print(sum(result[n])%1000000009)

    