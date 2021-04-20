#https://www.acmicpc.net/problem/2776
#백준 2776번 암기왕(정렬)
#import sys
#input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    note1 = set(list(map(int, input().split())))
    m = int(input())
    note2 = list(map(int, input().split()))
    check = set(note2)
    result = check-note1
    for i in note2:
        if i in result:
            print(0)
        else:
            print(1)