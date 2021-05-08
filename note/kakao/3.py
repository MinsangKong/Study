def solution(n, k, cmd):
    answer = ['O']*n
    idx = k
    cnt = 0
    deleted = []
    while cnt < len(cmd):
        if cmd[cnt][0] == 'C':
            answer.pop(idx)
            deleted.append(idx)
            if idx >= len(answer):
                idx = len(answer)-1
        elif cmd[cnt][0] == 'Z':
            num = deleted.pop()
            answer.insert(num,'O')
            if num <= idx:
                idx+=1
        elif cmd[cnt][0] == 'U':
            idx-=int(cmd[cnt][2]) 
        else:
            idx+=int(cmd[cnt][2])
        cnt+=1
        print(idx)
    if deleted:
        for i in range(len(deleted)-1,-1,-1):
            num = deleted[i]
            answer.insert(num,'X')
    return ''.join(answer)
print(solution(8,2,["D 2","C","C","C","U 2","Z","Z","Z","C"]))