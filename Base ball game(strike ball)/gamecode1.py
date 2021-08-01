from random import *

answer = str(randint(1, 999))

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
            if answer[i] == guess[i]:
                strike = strike + 1
            elif guess[i] in answer:
                ball = ball +1

        print('{}strike  {}ball'.format(strike, ball))