from sys import stdin

n = int(stdin.readline().strip())
a = [(int(stdin.readline().strip()), i) for i in range(n)]
r = [a[i][1] + 1 for i in range(n)]
sorted_list = [0] * n


def merge_sort(l):
    if len(l)==1:
        return l
    n,m=len(l),len(l)//2
    l1=l[:m]
    l2=l[m:]
    l1=merge_sort(l1)+[(0,0)]
    l2=merge_sort(l2)+[(0,0)]
    i1=i2=0
    for i in range(n):
        if l1[i1][0]>l2[i2][0]:
            l[i]=l1[i1]
            i1+=1
            continue
        else:
            l[i]=l2[i2]
            r[l2[i2][1]]-=(m-i1)
            i2+=1
    return l
merge_sort(a)
s='\n'.join(map(str,r))
print(s)