def solution(k, m, score):
    list = []
    for i in range(1, m+1):
        list.append(sorted(score)[-i])
    answer = min(list) * m * (상자의 개수)
    
    return list #사과고르기