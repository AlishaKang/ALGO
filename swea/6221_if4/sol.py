import sys
sys.stdin = open('input.txt', encoding='utf-8')

man1 = input()
man2 = input()

rsp = ['가위', '바위', '보']

# index()를 사용하면 그 값의 위치를 알 수 있다.

if rsp.index(man1) == rsp.index(man2):
    print('Result : Draw')
elif (rsp.index(man1) - rsp.index(man2)) == 1:
    print('Result : Man1 Win!')
elif(rsp.index(man2) - rsp.index(man1)) == 1:
     print('Result : Man2 Win!')
else:
    if rsp.index(man1) == 0:
        print('Result : Man1 Win!')
    else: 
        print('Result : Man2 Win!')
