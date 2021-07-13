from sys import stdin
from math import ceil, log2


def make_tree(start, end, idx):
    if start == end:
        tree[idx] = [arr[start], arr[start]]
    else:
        mid = (start + end) // 2
        make_tree(start, mid, idx*2)
        make_tree(mid+1, end, idx*2+1)
        tree[idx] = [min(tree[idx*2][0], tree[idx*2+1][0]), max(tree[idx*2][1], tree[idx*2+1][1])]


def solve(start, end, idx, a, b):
    mid = (start + end) // 2
    if (start == a and end == b) or start == end:
        return tree[idx]
    if b <= mid:
        return solve(start, mid, idx*2, a, b)
    if a > mid:
        return solve(mid+1, end, idx*2+1, a, b)
    left = solve(start, mid, idx*2, a, mid)
    right = solve(mid+1, end, idx*2+1, mid+1, b)
    return [min(left[0], right[0]), max(left[1], right[1])]

n, m = map(int, stdin.readline().split())
arr = [0]
for _ in range(n):
    arr.append(int(stdin.readline()))


tree = [0 for i in range(2<<(ceil(log2(n))))]
make_tree(1, n, 1)
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    res = solve(1, n, 1, a, b)
    print(res[0], res[1])