import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1 + T):
    N, M = list(map(int, input().split())) #글자판크기 #회문길이

    matrix = [] #글자판

    for _ in range(N):
        matrix.append(input())

    result = ''
    # 가로 기준점 / 회문의 시작점을 잡기 위한 반복문
    for i in range(N):
        for j in range(N-M+1):
            
            for row in range(M//2):
                # front : 맨앞글자부터 한칸씩 증가
                f = matrix[i][j+row]
                # back : 맨뒷글자부터 한칸씩 감소
                b = matrix[i][j+M-1-row]

                # 앞뒤가 똑같다면 다음글자 확인하기
                if f == b:
                    continue
                # 앞뒤가 다르다면, 더 확인할 필요가 없으니 확인정지
                else:
                    break
            #break를 만나지 않은 경우 => 끝까지 반복, 회문 찾은 경우
            else:
                for a in range(M):
                    result += matrix[i][j+a]


    # 세로 기준점 / 회문의 시작점을 잡기
    for j in range(N):
        for i in range(N-M+1):
            for col in range(M//2):
                f = matrix[i+col][j]
                b = matrix[i+M-1-col][j]

                if f == b:
                    continue
                else:
                    break
            else:
                for a in range(M):
                    result += matrix[i+a][j]
    print(result)
