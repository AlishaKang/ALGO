def solution(M, N):
    if M > 1 and N > 1:
        answer = M*N-1
    elif M == 1 and N == 1:
        answer = 0
    else:
        if M > 1:
            answer = M-1
        else:
            answer = N-1
    return answer

print(solution(2,2))