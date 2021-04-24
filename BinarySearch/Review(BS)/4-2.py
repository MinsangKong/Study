import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
ans = []
for b in B:
    if b in A: ans.append("1")
    else: ans.append("0")
print(" ".join(ans))