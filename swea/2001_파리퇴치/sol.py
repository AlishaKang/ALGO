import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split()) #전체영역크기 #파리채크기
    numbers = [list(map(int, input().split())) for i in range(N)]

    kills = []

    # 파리채로 내려칠 곳
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            # 해당 위치 타격 시 잡을 수 있는 파리의 숫자
            for k in range(M):
                for l in range(M):
                    fly += numbers[i+k][j+l]
            kills.append(fly)

    print('#'+str(tc), max(kills))
            
