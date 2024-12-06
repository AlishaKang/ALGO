def solution(n):
    answer = 0
    for i in range(2, n):
        if n % i == 0:
            pass
        else:
            answer += 1 
    return answer