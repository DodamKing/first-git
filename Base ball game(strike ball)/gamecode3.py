from random import *

# 중복회피
number_list = [i for i in range(10)] 

while True: # 첫자리 숫자가 0되는 것을 제외
    shuffle(number_list)
    if number_list[0] != 0:
        break
answer = str(number_list[0]) + str(number_list[1]) + str(number_list[2])
print(answer)

while True:
    try: # 예외처리
        guess = input('숫자를 입력하세요(종료: q): ')
        if guess == 'q':
                break

        elif 1 <= int(guess) <= 999: # 세자리 숫자일 때만 코드 실행
            if answer == guess:
                print('{} 정답입니다.'.format(answer))
                break
            else:
                strike = 0
                ball = 0

                for i in range(3):
                    if answer[i] == guess[i]: # 정답의 i번째 값과 추측의 i번째 값이 같으면 스트라이크
                        strike = strike + 1
                    elif guess[i] in answer: # 추측한 숫자가 정답에 들어있으면 볼
                        ball = ball + 1

                print('{}strike {}ball'.format(strike, ball))
        else:
            raise # 아니면 일부러 오류 발생
    
    except: # 오류면 
        print('세자리 숫자를 입력하세요.')