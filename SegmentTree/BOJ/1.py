#https://www.acmicpc.net/problem/2042
#백준 2042 구간 합 구하기(세그먼트트리)
#import sys
#input = sys.stdin.readline

def init(s,e,idx):
    if s == e:
        trees[idx] = nums[s]
        return trees[idx]
    mid =(s+e)//2
    trees[idx] = init(s,mid,idx*2)+init(mid+1,e,idx*2+1)
    return trees[idx]
    
def query(s,e,idx,l,r):
    if l > e or r < s:
        return 0
    if l <= s and e <= r:
        return trees[idx]
    mid = (s+e)//2
    return query(s,mid,idx*2,l,r)+query(mid+1,e,idx*2+1,l,r)

def update(s,e,idx,k,diff): #k는 바꾸고자 하는 인덱스 번호,diff는 바꾸는 값
    if not (s<=k<=e):
        return
    trees[idx] += diff
    
    if s != e:
        mid = (s+e)//2
        update(s,mid,idx*2,k,diff)
        update(mid+1,e,idx*2+1,k,diff)
    
n, m, k = map(int, input().split())
nums = [0]+[int(input()) for _ in range(n)]
trees = [0]*(n*4)
info = [list(map(int, input().split())) for _ in range(m+k)]
        

init(1,n,1)
#print(trees)
for a,b,c in info:
    if a == 1:
        update(1,n,1,b,c-nums[b])
        nums[b] = c
    else:
        print(query(1,n,1,b,c))
    #print(trees)