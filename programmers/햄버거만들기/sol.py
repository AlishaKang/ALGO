def solution(ingredient):
    box = []
    cnt = 0
    for i in ingredient:
        box.append(i)
        if box[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for _ in range(4):
                box.pop()
    
    return cnt

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))