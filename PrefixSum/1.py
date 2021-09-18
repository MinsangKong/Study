#https://www.acmicpc.net/problem/21318
#백준 21318번 피아노 체조(누적합)
#import sys
#input = sys.stdin.readline

n = int(input())
difficulty = list(map(int, input().split()))
prefixSum = [0]*n

for i in range(1,n):
    prefixSum[i]+=prefixSum[i-1]
    if difficulty[i] < difficulty[i-1]:
        prefixSum[i]+=1
        
for _ in range(int(input())):
    x, y = map(int, input().split())
    print(prefixSum[y-1]-prefixSum[x-1])