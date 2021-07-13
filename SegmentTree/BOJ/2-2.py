import sys
input=sys.stdin.readline
n,q=map(int,input().split())
a=[*map(int,input().split())]
bit=[0]+a[:]
for i in range(1,n+1):
    i1=i+(i&-i)
    if i1<=n: bit[i1]+=bit[i]
def getSum(i):
    s=0
    while i:
        s+=bit[i]
        i-=i&-i
    return s
def update(i,x):
    while i<=n:
        bit[i]+=x
        i+=i&-i
for _ in range(q):
    i,j,x,y=map(int,input().split())
    if i>j: i,j=j,i
    print(getSum(j)-getSum(i-1))
    d=y-a[x-1]
    a[x-1]=y
    update(x,d)
'''
팬윅트리를 활용한 방법
https://www.acmicpc.net/blog/view/21 참고
'''