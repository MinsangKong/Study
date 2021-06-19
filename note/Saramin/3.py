import sys
input = sys.stdin.readline
import bisect

n, a, b = map(int, input().split())

result = 1983
dp = [0]*n
dp[0] = 1983
check = [1983]
for i in range(1,n):
    dp[i] = (dp[i-1]*(a+b))%20090711
    if check[-1] < dp[i]:
        check.append(dp[i])
    else:
        check.insert(bisect.bisect_left(check,dp[i]),dp[i])
    result = (result+check[i//2]) % 20090711
    
print(result)