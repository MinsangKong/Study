#https://www.acmicpc.net/problem/3079
#백준 3079번 입국심사(이분탐색)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
times = []
for _ in range(n):
    times.append(int(input()))
    
start = 1
end = min(times)*m
while start <= end:
    mid = (start+end)//2
    cnt = 0
    for time in times:
        cnt+=mid//time
    if cnt >= m:
        end = mid-1
    else:
        start = mid+1
        
print(start)