n, m = map(int, input().split()) #이분탐색으로 감을 도자히 못잡아서 검색
arr = list(map(int, input().split())) 
cnt = 0 
lo, hi = 0, 1 #low pointer와 high pointer
tmp = arr[lo] 
while lo < n: 
    if tmp == m: 
        cnt += 1 
        tmp -= arr[lo]
        lo += 1 
        
    if hi == n and tmp < m: 
        break 
    elif tmp < m: 
        tmp += arr[hi] 
        hi += 1 
    elif tmp > m: 
        tmp -= arr[lo]
        lo += 1 
            
print(cnt)