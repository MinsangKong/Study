#https://www.acmicpc.net/problem/1615
#백준 1615번 교차개수세기(세그먼트트리)
import sys
input = sys.stdin.readline

def query(s,e,idx,l,r):
    if r < s or l > e:
        return 0
    if s >= l and e <= r:
        return tree[idx]
    else:
        mid = (s+e)//2
        return query(s,mid,idx*2,l,r)+query(mid+1,e,idx*2+1,l,r)
    
def update(s,e,idx,k,diff):
    if not (s<=k<=e):
        return
    tree[idx] += diff
    if s != e:
        mid = (s+e)//2
        update(s,mid,idx*2,k,diff)
        update(mid+1,e,idx*2+1,k,diff)

n, m = map(int, input().split())
tree = [0]*(4*n)
check = []

for _ in range(m):
    a,b = map(int, input().split())
    check.append([a,b])
    
check.sort(key = lambda x : (x[0],x[1]), reverse = True)
result = 0

for i in range(m):
    b = check[i][1]
    result += query(1,n,1,1,b-1)
    update(1,n,1,b,1)
    #print(tree)
    
print(result)