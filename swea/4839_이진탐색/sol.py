import sys
sys.stdin = open('input.txt')

T = int(input())

def search(P, target):
    left = 1
    right = P
    count = 0
    while left <= right:
        mid = int((left + right) / 2)
        if mid == target:
            break
        elif mid < target:   0 t 200  400
            left = mid
            count += 1
        elif mid > target:
            right = mid
            count += 1
    return count

for tc in range(1, 1 + T):
    P, A, B = map(int, input().split())

    countA = search(P, A)
    countB = search(P, B)

    if countA > countB:
        result = 'B'
    elif countA < countB:
        result = 'A'
    else:
        result = 0
    print(f'#{tc} {result}')

