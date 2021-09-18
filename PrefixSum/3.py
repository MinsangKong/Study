#https://www.acmicpc.net/problem/10713
#백준 10713번 기차 여행(누적합)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0]*(n+1)

for i in range(1,m):
    if nums[i] > nums[i-1]:
        dp[nums[i]] -= 1
        dp[nums[i-1]] += 1
    else:
        dp[nums[i]] += 1
        dp[nums[i-1]] -= 1
        
for i in range(1,n+1):
    dp[i] += dp[i-1]
        
#print(dp)
result = 0

for i in range(n-1):
    ticket, passIC, costIC = map(int, input().split())
    result += min(dp[i+1]*ticket, dp[i+1]*passIC+costIC)
    #print(result)
    
print(result)

'''
문제의 포인트는 방문 횟수를 기록하는 것
기차의 이동 방식은 1->2->3->... 이런 식이기 때문에 nums[i]~nums[i+1] 구간에만
횟수를 체크해야 하기 때문에 누적합 방식을 이용하여 해당 구간의 횟수만 더해주면
방문 횟수를 구할 수 있다.
'''