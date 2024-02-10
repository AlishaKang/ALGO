def solution(a, b):
    answer = []
    length = len(a)
    for i in range(length):
        answer.append(a[i] * b[i])
            
    return sum(answer)