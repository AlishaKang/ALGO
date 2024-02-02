def solution(n):
    answer = []
    a = len(str(n)) #5
    for i in range(1, a+1):
        answer.append(int(str(n)[-i]))  #-1~-5
    return answer

print(solution(12345))

# a= list(range(1, 6))
# print(a)