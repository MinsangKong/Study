#https://www.acmicpc.net/problem/2002
#백준 2002번 추월(구현, 딕셔너리)
#import sys
#input = sys.stdin.readline
n = int(input())
entres = {}
exit = {}
cnt = 0
for i in range(n):
    ent = input().rstrip()
    entres[ent] = i
for i in range(n):
    ex = input().rstrip()
    exit[i]=entres[ex]
    
for i in range(n):
    for j in range(i+1,n):
        if exit[i] > exit[j]:
            cnt+=1
            break

print(cnt)
'''
아이디어를 떠올리기 힘들었지만 단순하게 생각하면 출구를 기준으로 내 뒤에 있는 차량이
입구를 기준으로 내 앞에 있었다면 나는 추월한 셈이다. 이를 기준으로 횟수를 늘리면 되는
문제였다. 굳이 for문으로 내 입구 순서와 출구 순서를 찾은 뒤 비교하려고 해서 문제만
엄청 꼬아서 풀었다...
'''