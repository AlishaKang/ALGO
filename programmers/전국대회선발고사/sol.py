def solution(rank, attendance):
    students = sorted([(r, i) for i, r in enumerate(rank)]) 
    #r을 기준으로 sorted해야해서 r이 앞으로 나옴

    selected = [] #true only

    for r, i in students:
        if attendance[i]:
            selected.append(i)
            if len(selected) == 3:
                break
    answer = 10000*selected[0] + 100*selected[1] + selected[2]
    return answer

print(solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False]))