#Q10 자물쇠와 열쇠
def rotate(arr):
    length = len(arr)
    rot = [[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            rot[j][length-1-i]=arr[i][j]
    return rot

def check(keyX, keyY, key, lock, size, start, end):
    pad = [[0]*size for _ in range(size)]
    for i in range(len(key)):
        for j in range(len(key)):
            pad[keyX+i][keyY+j] +=key[i][j]
    for i in range(start, end):
        for j in range(start, end):
            pad[i][j] += lock[i-start][j-start]
            if pad[i][j] != 1:
                return False
    return True

def solution(key, lock):
    start = len(key)-1
    end = start+len(lock)
    size = len(lock)+2*len(key)
    
    #rotate 횟수
    for k in range(0,4):
        for i in range(end):
            for j in range(end):
                if check(i, j, key, lock, size, start, end):
                    return True
        key = rotate(key)
    return False