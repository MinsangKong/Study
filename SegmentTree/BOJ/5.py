#https://www.acmicpc.net/problem/2243
#백준 2243번 사탕상자(세그먼트 트리)
#import sys
#input = sys.stdin.readline
INF = 1000000

def query(s,e,idx,point): #해당하는 사탕의 맛
    if s == e:
        return s
    mid = (s+e)//2
    if tree[idx*2] >= point: 
        #왼쪽 자식이 seq보다 크다면 왼쪽에 사탕이 있으므로 왼쪽으로
        return query(s,mid,idx*2,point)
    else:
        #그렇지 않다면 오른쪽에 사탕이 있으므로 왼쪽 구간합만큼 빼준뒤 오른쪽으로
        return query(mid+1,e,idx*2+1,point-tree[idx*2])
    
def update(s,e,idx,k,diff):
    if not(s<=k<=e):
        return
    tree[idx]+=diff
    if s != e:
        mid = (s+e)//2
        update(s,mid,idx*2,k,diff)
        update(mid+1,e,idx*2+1,k,diff)
    
n = int(input())
tastes = [0]*(INF+1)
tree = [0]*(INF*4)

for _ in range(n):
    data = list(map(int, input().split()))
    if len(data) == 2:
        num = data[1]
        ans = query(1,INF,1,num)
        print(ans)
        tastes[ans]-=1
        update(1,INF,1,ans,-1)
    else:
        b, c = data[1], data[2]
        tastes[b]+=c
        update(1,INF,1,b,c)
    print(tree)