#https://www.acmicpc.net/problem/1275
#백준 1275번 커피숍2(세그먼트 트리)
#import sys
#input = sys.stdin.readline

def init(s,e,idx):
    if s == e:
        tree[idx] = nums[s] 
        return tree[idx]
    mid = (s+e)//2
    tree[idx] = init(s,mid,idx*2)+init(mid+1,e,idx*2+1)
    return tree[idx]

def query(s,e,idx,l,r):
    if l > e or s > r:
        return 0
    if l <= s and e <= r: #완벽하게 범위가 포개어 지는 경우
        return tree[idx]
    mid = (s+e)//2
    return query(s,mid,idx*2,l,r)+query(mid+1,e,idx*2+1,l,r)

def update(s,e,idx,k,diff):
    if not (s<=k<=e):
        return
    tree[idx]+=diff
    if s != e:
        mid = (s+e)//2
        update(s,mid,idx*2,k,diff)
        update(mid+1,e,idx*2+1,k,diff)

n, q = map(int, input().split())
nums = [0]+list(map(int, input().split()))
info = [list(map(int, input().split())) for _ in range(q)]
tree = [0]*(4*n)

init(1,n,1)

for x,y,a,b in info:
    if x > y:
        print(query(1,n,1,y,x))
    else:
        print(query(1,n,1,x,y))
    update(1,n,1,a,b-nums[a])
    nums[a] = b
    print(tree)