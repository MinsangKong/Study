#https://www.acmicpc.net/problem/2143
#백준 2143번 두 배열의 합(이분탐색)
#import sys
#input = sys.stdin.readline
from collections import defaultdict

t = int(input())
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

dictA = defaultdict(int)

result = 0

for i in range(n):
    for j in range(i, n):
        dictA[sum(arr1[i:j+1])] += 1

for i in range(m):
    for j in range(i, m):
        result += dictA[t-sum(arr2[i:j+1])]
        
print(result)
'''
defaultdict를 사용하면 자동적으로 모든 값에 0이 들어가기 때문에 값 여부를 체크하는
구문을 작성할 필요가 없어진다.
'''