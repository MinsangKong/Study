#https://www.acmicpc.net/problem/14002
#백준 14002번 가장 긴 증가하는 부분 수열 4
#이전 문제는 풀었지만 최대값에서 그 순열의 값을 어떻게 구해야할지 몰랐음. 해설보고도 이해가 어려움
n = int(input())
lst = list(map(int, input().split()))

dp = [1 for i in range(n)]
array = [[x] for x in lst]

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            if dp[j] + 1 > dp[i]: #부분 순열의 길이 비교
                array[i] = array[j] + [lst[i]]
                dp[i] = dp[j] + 1
length = 0
flag = 0
for i in range(n):
    if length < dp[i]:
        flag = i
        length = dp[i]
print(length)
print(*array[flag])