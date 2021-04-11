#https://www.acmicpc.net/problem/1822
#백준 1822번 차집합(정렬)
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

a = set((list(map(int, sys.stdin.readline().split()))))
b = set((list(map(int, sys.stdin.readline().split()))))

a_sorted = sorted(list(a.difference(b)))
if a_sorted:
    print(len(a_sorted))
    for i in a_sorted:
        print(i, end=' ')
else:
    print(0)