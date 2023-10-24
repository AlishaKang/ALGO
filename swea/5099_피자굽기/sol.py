import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split()) #화덕크기 #피자개수
    pizza = list(map(int, input().split())) #최초 치즈양
    cheese = []

    for i in range(M):
        cheese.append([i+1, pizza[i]]) #최초 치즈양의 피자들에게 index붙임
    oven = cheese[:N] #피자넣기
    remain = cheese[N:] #화덕 밖 남은피자

    while len(oven) > 1:
        check = oven.pop(0) #제일먼저 넣은피자 꺼내기
        check[1] //= 2 #다음 피자의 남은 치즈 확인하기
        if check[1] == 0: #다 녹은 경우
            if remain:
                oven.append(remain.pop(0))
            else:
                oven.append(check)
    print(f'#{tc} {oven[0][0]}')

