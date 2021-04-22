#https://www.acmicpc.net/problem/8983
#백준 8983번 사냥꾼(정렬)
#import sys
#input = sys.stdin.readline
import bisect

m, n, l = map(int, input().split())
place = list(map(int, input().split()))
animals = []
for _ in range(n):
    animals.append(list(map(int, input().split())))
    
place.sort()
result = 0
bisects = []
for i in animals:
    bisects.append(bisect.bisect(place, i[0]))
    
for i in range(n):
    if bisects[i] < m and place[bisects[i]] - animals[i][0] + animals[i][1] <= l:
        result +=1
    elif 0 < bisects[i] and animals[i][0] - place[bisects[i]-1]+ animals[i][1] <= l:
        result +=1
        
print(result)
'''
https://velog.io/@gojaegaebal/201223-%EA%B0%9C%EB%B0%9C%EC%9D%BC%EC%A7%8016%EC%9D%BC%EC%B0%A8-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-bisect-%ED%95%A8%EC%88%98-%ED%99%9C%EC%9A%A9-feat.%EB%B0%B1%EC%A4%80-8983%EB%B2%88
bisect 함수를 활용해서 이분 탐색없이도 구현할 수 있음
'''