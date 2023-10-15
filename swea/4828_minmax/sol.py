import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    numbers = list(map(int, input().split()))

    print('#' + str(tc), max(numbers) - min(numbers))