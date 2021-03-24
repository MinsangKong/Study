#https://www.acmicpc.net/problem/2002
#백준 2002번 추월(구현, 스택)
#import sys
#input=sys.stdin.readline

N=int(input())
dk=[input() for i in range(N)]
ys=[input() for i in range(N)]
count=0
for i in range(N) :
    a=dk.pop(0)
    while True :
        if a not in ys :
            break
        elif a!=ys[0] :
            ys.pop(0)
            count+=1
        else :
            ys.pop(0)
            break
print(count)
'''
다른 사람이 작성한 코드를 보니까 굳이 딕셔너리로 안 만들고 stack을 활용해서 
기존과 순서가 다른 차량을 pop하는 식으로 문제를 푸는 방식이 깔끔하고
속도면에서도 훨씬 빨랐다.
'''