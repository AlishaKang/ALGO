# def solution(s):
#     answer = ''
#     length = len(s)
#     for i in range(length):
#         if i % 2 == 0: #짝수면 대문지
#             answer += s[i].upper()
#         else:
#             answer += s[i].lower()
#     return answer

def solution(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer+= ' '
    return answer[0:-1]

print(solution("What a happy Day"))