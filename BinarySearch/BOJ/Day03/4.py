#https://www.acmicpc.net/problem/15810 풍선 공장
n , m = map(int, input().split())
arr = list(map(int, input().split()))
    
end= min(arr)*m #최대 걸리는 시간은 최소 풍선 부는 시간 * 수
start = min(arr) #하나당 걸리는 최소 시간
while start +1 < end:
    mid = (start+end)//2
    total = 0
    for i in arr:
        total += (mid//i)
    if total >= m:
        end = mid
    else :
        start = mid

print(end)