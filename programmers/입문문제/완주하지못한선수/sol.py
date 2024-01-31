def solution(participant, completion):
    p = sorted(participant)
    c = sorted(completion)
    
    for i in range(len(completion)):
        if p[i] != c[i]:
            return p[i] #c[i]로 하면 완주자니까 p[i]로
    
    return p[-1]
    