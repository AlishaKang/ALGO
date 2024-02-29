def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        a = numbers[i] + numbers[i+1]
        if a not in answer:
            answer.append(a)
    return answer