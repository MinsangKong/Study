#12 기둥과 보
def is_possible(result):
    for x, y, structure in result:
        if structure == 0: #기둥일 때
            if y == 0 or  (x-1,y,1) in result or (x,y,1) in result or (x,y-1,0) in result :
                continue
                #y == 0 : 기둥이 땅에 닿아 있을 때
                #(x-1,y,1) in result or (x,y,1) in result  : 보의 끝 부분에 위치할 때
                #(x,y-1,0) in result : 다른 기둥 위에 있을 때
            else:
                return False
        elif structure == 1:
            if (x,y-1, 0) in result or (x+1,y-1,0) in result or ((x-1,y,1) in result and (x+1,y,1) in result):
                continue
                #(x,y-1, 0) in result or (x+1,y-1,0) in result : 기둥 위에 있을 때
                #((x-1,y,1) in result and (x+1,y,1) in result) : 양쪽 끝 부분이 다른 보와 연결되어 있을 때
            else:
                return False
    return True

def solution(n, build_frame):
    #list+tuple을 활용한 것보다 set을 활용하는 것이 시간면에서 더 효율적이었다.
    result = set()
    for x,y,structure,do in build_frame:
        if do == 1: #일단 실행한 다음에 문제가 있으면 되돌림
            result.add((x,y,structure))
            if not is_possible(result):
                result.remove((x,y,structure))
        elif do == 0:
            result.remove((x,y,structure))
            if not is_possible(result):
                result.add((x,y,structure))
    result = [list(i) for i in result]
    return sorted(result, key = lambda x: (x[0],x[1],x[2]))
'''
해설을 보고 풀면 꽤 쉬운 문제였는데 문제를 보고 감을 못잡아서 엄청 해맸다.
기둥과 보의 조건을 단순하게 if문으로 적용하기만 하면 되는 문제였지만
문제를 보고 그게 안 떠올랐다....
'''