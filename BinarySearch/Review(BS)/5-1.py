#https://www.acmicpc.net/problem/2805
#백준 2805번 나무 자르기(이분탐색)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()
start = 0
end = trees[-1]
result = 0
while start <= end:
    mid = (start+end)//2
    sub = 0
    for i in trees:
        if i > mid:
            sub+=i-mid
    if sub >= m:
        result = mid
        start = mid + 1    
    else:
        end = mid - 1
            
print(result)
'''
파이썬에서 시간초과가 계속 발생해서 pypy3로 해결. 
파이썬으로 해결한 사람들의 코드를보니까 같은 입력이 매우 많았다. 
그래서 Counter로 횟수를 센 다음에 dictionary를 사용하여 답을 구했다.
'''