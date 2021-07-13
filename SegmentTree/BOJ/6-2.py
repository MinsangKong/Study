import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())

def update(idx, val):
	idx += L
	seg[idx] = val
	idx //= 2
	while idx:
		seg[idx] = seg[idx*2] + seg[idx*2+1]
		idx //= 2

def query(l, r):
	l, r = l+L, r+L
	ret = 0 
	while l <= r:
		if l%2 == 1:
			ret += seg[l]
			l += 1
		if r%2 == 0:
			ret += seg[r]
			r -= 1
		l //= 2; r //= 2
	return ret

N = int(input())
L = 2 ** N.bit_length()
seg = [0] * (L*2)

nums = [int(input()) for i in range(N)]
k = [x for x in sorted(nums)]
d = {}
for i in range(N):
	d[k[i]] = i
ans = []
for i in nums:
	update(d[i], 1)
	ans.append(query(d[i], N))
print(*ans, sep='\n')