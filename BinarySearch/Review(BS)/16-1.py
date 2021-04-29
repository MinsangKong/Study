#https://www.acmicpc.net/problem/2352
#백준 2352번 반도체 설계(이분탐색,DP,lis)
#import sys
#input = sys.stdin.readline
import bisect

n = int(input())
ports = list(map(int, input().split()))

dp = [ports[0]]
for i in range(1,n):
    if ports[i] > dp[-1]:
        dp.append(ports[i])
    else:
        dp[bisect.bisect(dp, ports[i])] = ports[i]
print(len(dp))
'''
가장 긴 증가하는 수열(lis)를 활용해서 푸는 문제였다. 아무리 봐도 그냥 풀기에는 시간 초과가
발생 할 것 같은 데 풀이법은 떠오르지 않아서 결국 구글링 후 이해했다. n이 작을 때에는
dp방식으로 lis를 구해도 괜찮지만 n이 클 경우 bs 방식으로 구해야 한다. 이 문제는
bisect를 활용해서 빠르게 구할 수 있었다.
'''