import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    

    def function(N): #N=세로
        if N % 10 == 0:
            if N == 10:
                return 1
            elif N == 20:
                return 3
            else:
                return function(N-10) + 2 * function(N-20)
    count = function(N)    
            
    print("#{} {}".format(tc, count))