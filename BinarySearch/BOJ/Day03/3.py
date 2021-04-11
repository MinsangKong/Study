#https://www.acmicpc.net/problem/13702 이상한 술집
n , k = map(int, input().split())
arr = []

for i in range(n):
    arr.append(int(input()))
    
end= max(arr)
start = 0
result = 0
while(start <= end):
    total = 0 
    mid = (start+end)//2
    for x in arr:
        if x > mid:
            total = total+(x//mid)
    if total < k:
        end = mid -1
    else:
        result = mid
        start = mid+1
print(result)