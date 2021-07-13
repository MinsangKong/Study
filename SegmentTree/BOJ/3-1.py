#https://www.acmicpc.net/problem/2357
#백준 2357번 최솟값과 최댓값(세그먼트트리)
import sys
input = sys.stdin.readline
INF = int(1e9)

def init_max(s,e,idx):
    if s == e:
        tree_max[idx] = nums[s]
        return tree_max[idx]
    mid = (s+e)//2
    tree_max[idx] = max(init_max(s,mid,idx*2),init_max(mid+1,e,idx*2+1))
    return tree_max[idx]

def init_min(s,e,idx):
    if s == e:
        tree_min[idx] = nums[s]
        return tree_min[idx]
    mid = (s+e)//2
    tree_min[idx] = min(init_min(s,mid,idx*2),init_min(mid+1,e,idx*2+1))
    return tree_min[idx]
    
def query_max(s,e,idx,l,r):
    if l > e or s > r:
        return -1
    if l <= s and e <= r: #완벽하게 범위가 포개어 지는 경우
        return tree_max[idx]
    mid = (s+e)//2
    return max(query_max(s,mid,idx*2,l,r), query_max(mid+1,e,idx*2+1,l,r))

def query_min(s,e,idx,l,r):
    if l > e or s > r:
        return INF
    if l <= s and e <= r: #완벽하게 범위가 포개어 지는 경우
        return tree_min[idx]
    mid = (s+e)//2
    return min(query_min(s,mid,idx*2,l,r), query_min(mid+1,e,idx*2+1,l,r))

n, m = map(int, input().split())
nums = [0]+[int(input()) for _ in range(n)]
tree_min = [0]*(4*n)
tree_max = [0]*(4*n)

init_max(1,n,1)
init_min(1,n,1)

for _ in range(m):
    a,b = map(int, input().split())
    print(query_min(1,n,1,a,b), end = ' ')
    print(query_max(1,n,1,a,b))