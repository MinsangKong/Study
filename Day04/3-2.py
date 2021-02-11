n = int(input()) #감을 못잡겠어서 구글 검색
k = int(input()) 
s, e = 1, k 
while s <= e: 
    m = (s+e)//2 #m은 B리스트를 일렬로 나열했을 때 cnt번째 값
    cnt = 0 #m보다 작은 값의 갯수가 cnt
    for i in range(1, n+1): 
        cnt += min(n, m//i) 
    if cnt < k:
        s = m+1 
    else: 
        e = m-1 
print(s) #left를 반환하는 이유는 동일한 값을 가질 경우 가장 작은 lower_bound가 답이기 때문

'''
i번째 행에 있는 값은 모두 i*j로 이루어진 i의 배수들이고, i번째 행의 최댓값은 i*n이다. 
 따라서 i번째 행에서 m보다 작은 값의 개수는 m//i나 n이 된다.
'''