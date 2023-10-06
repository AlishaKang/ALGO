def solution(n):
    answer = 0
    
    numbers = range(1, n+1)

    for number in numbers:
        if number % 2 == 0:
            answer = answer + number

    return answer

print(solution(10)) #30
print(solution(4)) #6