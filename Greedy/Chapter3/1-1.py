#chapter3 그리디 모험가 길드
#import sys
#input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
cnt = 0
result = [0] * (n+1)
arr.sort()

for i in arr:
    result[i]+=1
    
for i in range(1,n+1):
    cnt+=result[i]//i
    
print(cnt)
'''
예제를 많이 돌려봐도 답 자체는 동일하게 나오지만 for문을 2번 돌린다는 점에서 내 코드가
더 비효율적이다.
'''