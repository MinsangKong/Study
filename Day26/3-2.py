#https://www.acmicpc.net/problem/14567
#백준 14567번 선수과목(그래프이론, 위상정렬)
#import sys
#input = sys.stdin.readline

n,m = map(int,input().split())
adj = [[] for i in range(n+1)]
dp = [1]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    adj[b].append(a)
for i in range(1,n+1):
    for j in adj[i]:
        dp[i]=max(dp[i],dp[j]+1)
print(*dp[1:])
'''
가장 빠르게 푼 사람의 소스 코드를 보니까 위상 정렬 없이 dp로 해결했다.
간단하게 dp를 적용해서 풀 수 있었는데 위상정렬에 갖혀서 비효율적으로 해결했다...
아직 공부가 더 필요하다... 후...
'''