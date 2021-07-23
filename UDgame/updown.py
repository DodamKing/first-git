from random import *
answer = int(uniform(1, 999))

while True:
    try:
        x = int(input('숫자를 입력하세요: '))
        if answer == x:
            print('정답입니다.')
            break
        elif answer > x:
            print('Up')
        else:
            print('Down')
    except:
        print('1 에서 999 사이의 숫자를 입력하세요.')
