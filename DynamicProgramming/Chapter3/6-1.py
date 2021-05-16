#Q36 편집 거리

word1 = input()
word2 = input()

n = len(word1)
m = len(word2)
# 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
dp = [[0] * (m + 1) for _ in range(n + 1)]
# DP 테이블 초기 설정
for i in range(1, n + 1):
    dp[i][0] = i
for j in range(1, m + 1):
    dp[0][j] = j
# 최소 편집 거리 계산
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 대입
        if word1[i - 1] == word2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        # 문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
        else: # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중에서 최소 비용을 찾아 대입
            dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
print(dp[n][m]) 