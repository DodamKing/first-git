from random import *

answer = str(randint(100, 999))

print(answer)

while True:
    guess = input()

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
                ball = ball +1

        print('{}strike {}ball'.format(strike, ball))