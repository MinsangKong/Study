#https://www.acmicpc.net/problem/1208
#백준 1208번 부분 수열의 합 2 (Meet in the middle)
#import sys
#input = sys.stdin.readline

def dfs_Left(idx):
    global result
    global total
    if idx == mid :
        if total in count:
            count[total] += 1
        else:
            count[total] = 1
        return
    dfs_Left(idx+1)
    total += nums[idx]
    dfs_Left(idx+1)
    total -= nums[idx]
    
def dfs_Right(idx):
    global result
    global total
    if idx == n :
        if s-total in count:
            result += count[s-total]
        return
    dfs_Right(idx+1)
    total += nums[idx]
    dfs_Right(idx+1)
    total -= nums[idx]

n, s = map(int, input().split())
nums = list(map(int, input().split()))

mid = n//2
result = 0
count = dict()
total = 0

dfs_Left(0)
dfs_Right(mid)

print(result if s else result-1)
#https://blog.naver.com/kks227/221382873753 연관된 문제 정리