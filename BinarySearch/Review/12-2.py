#https://www.acmicpc.net/problem/3020
#백준 3020번 개똥벌레(이분탐색)
#import sys
#input = sys.stdin.readline
n, h = map(int, input().split())

down = [0] * (h + 1)  
up = [0] * (h + 1)  

min_count = n  
range_count = 0  

for i in range(n):
    if i % 2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1

for i in range(h - 1, 0, -1):
    down[i] += down[i + 1]
    up[i] += up[i + 1]

for i in range(1, h + 1):

    if min_count > (down[i] + up[h - i + 1]):
        min_count = (down[i] + up[h - i + 1])
        range_count = 1
    elif min_count == (down[i] + up[h - i + 1]):
        range_count += 1

print(min_count, range_count)
'''
서로의 끝은 닿지 않기에 범위를 h+1까지 고려해야 한다. 이 문제는 Prefix Sum을 구하는
문제이기 때문에 엄청 해맸다. 석순과 종유석의 누적합을 계산해야 시간초과가 발생하지 않는다.
'''