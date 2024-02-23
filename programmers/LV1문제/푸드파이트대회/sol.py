def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += food[i]//2 * str(i)
    reverse = answer[::-1]
    return answer +'0'+ reverse

# print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))