#Q13 치킨 배달
#import sys
#input = sys.stdin.readline
from itertools import combinations 
n, m = map(int, input().split())
city = []
chicken = []
home = []
for i in range(n):
    city.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i,j))
        elif city[i][j] == 1:
            home.append((i,j))
            
result = int(1e9)
for ch in combinations(chicken, m):
    dist = 0
    print(ch)
    for i in home:
        dist += min([abs(i[0]-j[0])+abs(i[1]-j[1]) for j in ch])
        if dist >= result:
            break
    if result > dist:
        result = dist

print(result)
'''
치킨 집의 좌표 조합을 combination을 적용해서 푸는 게 이 문제의 포인트였다.
초기 삼성 SW 문제라 아이디어만 잡으면 알고리즘 자체는 쉬웠다.
'''