# def solution(n):
#     answer = 0
#     for i in range(2, n):
#         if n % i == 0:
#             pass
#         else:
#             answer += 1 
#     return answer

# def solution(n):
#     answer = [] # 확인용
#     for i in range(2, n):
#         if n % i == 0:
#             pass
#         else:
#             answer.append(n) 
#     return answer

import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if isPrime(i) == True:
            answer += 1
    return answer

print(solution(10))