def bisect_left(arr, val):
    s, e = 0, len(arr)-1 
    while s <= e:
        m = (s+e)//2
        if arr[m] > val:
            e = m-1 
        else: s = m+1 
    return s 

n = input() 
dest = list(map(int, input().split())) 
link = [] 
for d in dest: 
    if not link or link[-1] < d:
        link.append(d) 
    else: 
        link[bisect_left(link, d)] = d 
print(len(link))
'''
biscet 함수를 활용하지 않고 이분 탐색으로 직접 구하는 방법이다.
'''