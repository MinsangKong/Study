#Q24번 안테나
#import sys
#input = sys.stdin.readline
from collections import Counter

n = int(input())
houses = list(map(int, input().split()))
counter = Counter(houses)

count = 0
total = sum(houses)
dist = sum(houses)
idx = 1

for i  in range(1,100001):
    total += count
    total -= n-count
    if dist > total:
        dist = total
        idx = i
    else:
        break
    count += counter[i]
    
print(idx)
'''
너무 충격적인 문제. 빠르게 푼 사람들은 그냥 정렬한 뒤 가장 중간에 있는 값을 출력해서
답을 구했다. 생각해보니 결과적으로 가장 중간이 있는 값이 평균이 될 수 밖에 없었다.
'''