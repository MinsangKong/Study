#https://www.acmicpc.net/problem/8983
#백준 8983번 사냥꾼(정렬)
#import sys
#input = sys.stdin.readline

m, n, l = map(int, input().split())
place = list(map(int, input().split()))
animal = []
for i in range(n):
    animal.append(list(map(int, input().split())))
place.sort()
animal.sort()
cnt = 0
check = -1
for i in place:
    point = check
    for j in range(check+1, n):
        if i+l < animal[j][0]:
            break
        else:
            if abs(i-animal[j][0])+animal[j][1] <= l:
                point = j
                cnt+=1
    check = point
                
print(cnt)
'''
입력의 개수가 100000 * 100000이라 시간 초과가 발생한다. 그러나 이분 탐색으로도 감이
안 잡혀서 결국 해설을 보고 이해했다.
'''