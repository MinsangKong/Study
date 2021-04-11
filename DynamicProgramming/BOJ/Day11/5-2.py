#https://www.acmicpc.net/problem/14002
#백준 14002번 가장 긴 증가하는 부분 수열 4
#다른 풀이법을 보고 이해함 
from collections import deque

n = int(input())

arr = list(map(int, input().split()))
dp = [0] * n
v = [0] * n
ans = deque()
maxNum = float('-inf')
maxIdx = 0

# 0부터 n 까지 돌면서 해당 수의 부분 수열 길이를 구합니다.
for i in range(0, n):
    dp[i] = 1
    v[i] = i
    # 자신보다 작은 수의 부분수열 길이가 자신보다 크거나 같으면,
    # 그 수 보다 부분수열의 길이를 1 늘려줍니다.
    # 또한 v라는 배열에는 자신보다 작은 부분수열의 인덱스를 저장해 놓습니다.
    for j in range(0, i):
        if dp[i] < dp[j] + 1 and arr[i] > arr[j]:
            dp[i] = dp[j] + 1
            v[i] = j
    if maxNum < dp[i]:
        maxIdx = i
        maxNum = dp[i]

# 아까 저장해놓은 v배열을 통해 가장 긴 부분수열을 구합니다.
idx = maxIdx
for _ in range(maxNum):
    ans.appendleft(arr[idx])
    idx = v[idx]

print(maxNum)
for x in ans:
    print(x, end=" ")