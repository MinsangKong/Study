#https://www.acmicpc.net/problem/2303
#백준 2303번 숫자게임(구현)
#import sys
#input = sys.stdin.readline
from itertools import combinations

N = int(input())
answer = 0
maxNum = 0
for i in range(1, N+1):
    numbers = list(map(int, input().split()))
    tmp = list(combinations(numbers, 3))
    t = list(map(lambda x: x%10 ,map(sum, tmp)))
    if max(t) >= maxNum:
        answer = i
        maxNum = max(t)
print(answer)
'''
 자체적으로 함수를 만드는 것보다 from itertools import combinations에서 combination을
 적용하는 것이 30ms 정도 빠르다
'''