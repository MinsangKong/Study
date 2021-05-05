#https://www.acmicpc.net/problem/16395
#백준 16395번 파스칼의 삼각형(DP)
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())
result = [[1]*i for i in range(1,n+1)]

for i in range(2,n):
    for j in range(i):
        if j != 0 :
            result[i][j] = result[i-1][j-1]+result[i-1][j]         
print(result[n-1][k-1])
'''
빠르게 푼 사람들의 코드를 보니까 factorial 활용해서 재귀로 풀었다.
'''