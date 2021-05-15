#https://www.acmicpc.net/problem/3649
#백준 3649번 로봇 프로젝트(이분탐색)
#import sys
#input = sys.stdin.readline

while True:
    try:
        x = int(input())
        n = int(input())
        hole = x*10000000
        toys = []

        for _ in range(n):
            toys.append(int(input()))
    
        toys.sort()
        start = 0
        end = n-1
        flag = False
        while start < end:
            total = toys[start]+toys[end]
            if total == hole:
                flag = True
                break
            elif total > hole:
                end -= 1
            else:
                start += 1
        if flag:
            print("yes",toys[start],toys[end])
        else:
            print("danger")
    except:
        break
'''
입력의 수를 정확하게 주지 않았기 때문에 try except문을 활용해서 문제를 풀어야 한다
'''