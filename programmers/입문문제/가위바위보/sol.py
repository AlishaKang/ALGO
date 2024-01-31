#풀이법1
def solution(rsp):
    d = {'0':'5', '2':'0', '5':'2'}
    return ''.join(d[i] for i in rsp)

#풀이법2
def solution(rsp):
    answer = ''

    for char in rsp:
        if char == '2':
            answer += '0'
        elif char == '0':
            answer += '5'
        else:
            answer += '2'

    return answer

print(solution('205'))
