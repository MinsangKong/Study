#import sys
#input = sys.stdin.readline

n = int(input().rstrip())

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    result = [[0]*2 for _ in range(n+1)]
    result[1][0] = 1
    result[1][1] = 1
    for i in range(2,n+1):
        result[i][0] = result[i-1][0]+result[i-1][1]
        result[i][1] = result[i-1][0]
        
    print(result[n][1])
'''
답이 피보나치 수열로 빠르게 구할 수 있는 이유는 새로 추가되는 원소가 0이면 그 전의 값들은
1이든 0이든 상관이 없기 때문이다. 뒷 자리가 1이면 그 전의 뒷자리는 0이어야만 만족할 수 있기
때문에 결과적으로 피보나치로 빠르게 구할 수 있었다. 후, dp 문제 풀 때 계속 1차원 배열만
떠오르는 게 문제다... 계속 2,3차원 배열로 구하는 문제는 엄청 해맨다.
'''