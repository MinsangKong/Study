#https://www.acmicpc.net/problem/17245
#백준 17245번 서버실(이분탐색)
#import sys
#input = sys.stdin.readline
import math

n = int(input())
computers = []
total = 0
length =0 
for _ in range(n):
    computer = list(map(int, input().split()))
    length = max(length, max(computer))
    total+=sum(computer)
    computers.append(computer)
    
start = 1
end = length
result = 0
while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in range(n):
        for j in range(n):
            if mid <= computers[i][j]:
                cnt+=mid
            else:
                cnt+=computers[i][j]
    if cnt >= math.ceil(total/2):
        result = mid
        end = mid-1
    else:
        start = mid+1
        
print(result)
'''
시간 초과 기준이 빡빡한 문제. pypy3로 제출하여 정답처리됨.
'''