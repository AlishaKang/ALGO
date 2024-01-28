def solution(num, total):
    list = []
    result =[]
    for i in range(num):
        list.append(i)
    a = sum(list)
    n = (total-a)//num 
    for i in range(num):
        result.append(i+n)
    return result

print(solution(3, 12))