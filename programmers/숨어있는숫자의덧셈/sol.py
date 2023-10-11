#풀이법1
def solution(my_string):
    answer = 0

    for char in my_string:
        if char.isdigit(): #숫자라면 T, 아니라면 F출력
            answer += int(char)

    return answer


#풀이법2
# def solution(my_string):
#     answer = 0

#     for char in my_string:
#         try:
#             answer += int(char)
#         except:
#             continue
#     return answer


print(solution("aAb1B2cC34oOp"))