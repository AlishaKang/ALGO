import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, 1 + T):
    dump = int(input()) #시행횟수
    boxes = list(map(int, input().split())) #박스숫자

    for i in range(dump):
        #최대높이
        top_box = boxes[0]
        top_box_idx = 0
        #최소높이
        down_box = boxes[0]
        down_box_idx = 0
       
       # 최대와 최소 높이 찾기
        for i in range(len(boxes)):
            if top_box < boxes[i]:
                top_box = boxes[i]
                top_box_idx = i

            if down_box > boxes[i]:
                down_box = boxes[i]
                down_box_idx = i
        
        # 평탄화
        boxes[top_box_idx] -= 1
        boxes[down_box_idx] += 1

        #전체 평탄화 횟수 전에 평탄화가 완료된 경우
        if boxes[top_box_idx] - boxes[down_box_idx] < 1:
            break
         
    

    result = print(f'#{tc} {top_box - down_box}')

      
