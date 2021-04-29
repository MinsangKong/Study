from collections import Counter

t=int(input())
n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int,input().split()))

def toPointer(lst,l):
    r=[]
    for i in range(l):
        temp=0
        for j in range(i,l):
            temp += lst[j]
            r.append(temp)
    return r

al = toPointer(a,n)
bl = toPointer(b,m)

result = 0
c=Counter(bl)
for i in al:
    result+=c[t-i]

print(result)
'''
시간적인 면에서는 딕셔너리를 사용하지 않고 단순하게 Counter함수를 활용하여 숫자를
세는 방식이 가장 빨랐다.
'''