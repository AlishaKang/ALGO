import sys
sys.stdin = open('input.txt')

T = int(input())

def search(idx):
    if idx >= N:
        return
    
    # 모든 경우의 수를 탐색
    for i in range(N):
        # print(idx, i, '=', numbers[idx][i])
        result.append(number[idx][i])
        search(idx + 1)
        result.pop()

for tc in range(1, 1 + T):
    N = int(input()) #NxN
    
    numbers = []
    for _ in range(N):
        number = list(map(int, input().split()))
        numbers.append(number) 

    # print(numbers)
    result = []

    search(0)