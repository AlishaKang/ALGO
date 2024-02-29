def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(1, len(numbers)-i):
            a = numbers[i] + numbers[i+j]
            if a not in answer:
                answer.append(a)
    return sorted(answer)