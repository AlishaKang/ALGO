import sys
sys.stdin = open('input.txt')

# K 한 번에 최대 이동거리
# N 종점
# M 정류장수

T = int(input()) #테스트 케이스 숫자

for tc in range(1, T+1):

    K, N, M = list(map(int, input().split()))

    bus_stop = list(map(int, input().split()))

    count = 0
    now = 0
    
    #충전할 필요가 없이 바로 도착하는 경우
    if K >= N:
        count = 0
    #충전을 하면서 지나가야 하는 경우
    else: 
        #버스가 종점에 도착하지 않은 경우 다시 반복
        while now < N:
            # 현재위치 now를 기준으로 최대로 갈 수 있는 범위를 찾는다.
            for i in range(now+K, now, -1):
                # 1. 최대 범위가 종점을 넘는 경우
                if i >= N:
                    now = N
                    break
                
                # 2. 최대범위가 종점을 넘지 않는 경우
                if i in bus_stop:
                    now = i
                    count += 1
                    break
                
            # 3. 현재 위치에서 최대 거리까지 다 확인을 했는데 충전소가 없다면=>도착불가능
            else:     
                count = 0
                now = N
    print(f'#{tc} {count}')