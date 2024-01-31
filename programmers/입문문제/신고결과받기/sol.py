def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x:0 for x in id_list}

    for r in set(report): #신고당한 횟수 레포트에 추가하기
        reports[r.split()[1]] += 1

    for r in set(report): #k번 이상 경고면 신고자에게 정지 메일 보내기
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    
    return answer