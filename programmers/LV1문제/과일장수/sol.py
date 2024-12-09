# def solution(k, m, score):
#     list = []
#     for i in range(1, m+1):
#         list.append(sorted(score)[-i])
#     answer = min(list) * m * (상자의 개수)
    
#     return list #사과고르기

def solution(k, m, score): # 사과 최대 점수, 한 상자 사과 개수, 사과 점수
    answer = 0 # 이익
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        if len(score[i:i+m]) == m:
            answer += min(score[i:i+m]) * m
    return answer