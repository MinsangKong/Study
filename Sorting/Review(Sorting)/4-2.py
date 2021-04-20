import sys
input=sys.stdin.readline
d={}
for _ in range(int(input())):
    t=int(input())
    d[t]=d.get(t,0)+1

print(max(sorted(d.keys()),key=lambda x:d[x]))
'''
가장 빠르게 문제를 해결하는 방식은 Counter를 활용해서 횟수를 세거나
딕셔너리를 활용해서 입력 받을 때 숫자를 세는 방식이 가장 빠르다.
'''