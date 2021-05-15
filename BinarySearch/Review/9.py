#https://www.acmicpc.net/problem/2343
#백준 2343번 기타 레슨(이분탐색)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
guitars = list(map(int, input().split()))

start = max(guitars)
end = sum(guitars)

while start <= end:
    mid = (start+end)//2
    cnt = 0
    size = 0
    for guitar in guitars:
        if size + guitar > mid:
            cnt += 1
            size = 0
        size += guitar
        
    if size != 0 :
        cnt+=1
    if cnt <= m:
        end = mid -1
    else:
        start = mid+1

print(start)