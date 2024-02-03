import math

def solution(n):
    a = math.sqrt(n)
    if a % 1 == 0:
        answer = (a+1)**2
    else: 
        answer = -1
    return answer

print(solution(121))