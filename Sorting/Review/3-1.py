#https://www.acmicpc.net/problem/10825
#백준 10825번 국영수(정렬)
#import sys
#input = sys.stdin.readline

n = int(input())
room = []
for _ in range(n):
    a,b,c,d = input().split()
    room.append((a,int(b),int(c),int(d)))
room.sort(key = lambda x: (-x[1],x[2],-x[3],x[0]))

for i in room:
    print(i[0])