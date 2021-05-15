#https://www.acmicpc.net/problem/9251
#백준 9251번 LCS(DP)
#import sys
#input = sys.stdin.readline

word1 = list(input().strip())
word2 = list(input().strip())
dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
for i in range(1,len(word1)+1):
    for j in range(1,len(word2)+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            
print(dp[-1][-1])
'''
word1과 word2에 가장 최근에 추가된 글자가 서로 같다면 두 글자가 추가되기 전 가장 큰
글자 수 + 1이 된다. 계속 if문으로 dp[i-1][j]이나 dp[i][j-1]에 1을 더해주는 방식이라고 생각해서
엄청 해매다가 풀었다... 
'''