n = int(input())
info = []

for _ in range(n):
    info.append(list(map(int, input().split())))
    
dp = [0]*(n+1)

for i in range(n):
    day, cost = info[i][0], info[i][1]
    dp[i+1] = max(dp[i],dp[i+1])
    if i+day <= n:
        dp[i+day]=max(dp[i+day], dp[i]+cost)
print(dp[n])
'''
max 함수의 사용을 줄이는 방향으로 문제를 풀었는데 속도는 이게 더 느렸다. why???
'''