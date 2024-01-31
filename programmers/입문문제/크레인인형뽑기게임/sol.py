def solution(board, moves):
    cnt = 0
    box = []
    
    for z in moves: #y축 숫자
        for j in range(len(board)):
            if board[j][z-1] == 0:
                continue
            else:
                box.append(board[j][z-1])
                board[j][z-1] = 0
                if len(box) > 1:
                    if box[-2] == box[-1]:
                        box.pop(-1)
                        box.pop(-1)
                        cnt+=2
                break
    return cnt

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))