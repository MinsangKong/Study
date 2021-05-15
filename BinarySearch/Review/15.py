#https://www.acmicpc.net/problem/13397
#백준 13397번 구간 나누기2(이분탐색)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = max(nums)
result = 0
while start <= end:
    mid = (start+end)//2
    diff_max = nums[0]
    diff_min = nums[0]
    cnt = 1
    print(start, mid, end)
    for i in range(1,n):
        diff_max = max(diff_max,nums[i])
        diff_min = min(diff_min,nums[i])
        if diff_max - diff_min > mid:
            cnt += 1
            diff_max = nums[i]
            diff_min = nums[i]
    if cnt <= m:
        result = mid
        end = mid-1
    else:
        start = mid+1
        
print(result)
'''
중량 제한은 BFS가 안 떠올라서 어려웠다면 구간 나누기는 단순하게 start, end값을 지정
하는 것 자체가 너무 어려웠다. 잘못된 방향으로 생각해서 결과적으로 오랜만에 해설을
보고 풀었다...
'''