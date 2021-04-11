#차집합으로 문제를 해결하면 이상없이 해결됨

import sys

n, m = map(int, sys.stdin.readline().split())

a = set((list(map(int, sys.stdin.readline().split()))))
b = set((list(map(int, sys.stdin.readline().split()))))

a_sorted = sorted(list(a.difference(b)))
if len(a_sorted) > 0:
    print(len(a_sorted))
    for i in a_sorted:
        print(i, end=' ')
else:
    print(0)