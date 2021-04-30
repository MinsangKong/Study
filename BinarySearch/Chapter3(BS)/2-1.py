#Q28 고정점 찾기
#import sys
#input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

start = 0
end = n-1
result = 0
while start <= end:
    mid = (start+end)//2
    if nums[mid] == mid:
        result = mid
        break
    elif nums[mid] < mid:
        start = mid + 1
    else:
        end = mid - 1
        
if result == 0:
    print(-1)
else:
    print(result)