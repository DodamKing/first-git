from tkinter import *
from random import *

win = Tk() 

win.title('Up & Down game') # 창 제목
win.geometry("300x500") # 창 크기

answer = int(randint(1, 999))

def reset():
    global answer 
    answer = int(randint(1, 999))
    # 라벨을 삭제하는 기능을 구현하고 싶다.

def UDcode():
    try :
        x = int(inp.get())
        if answer == x:
            label = Label(win, text='{} 정답입니다.'.format(x), font=('맑은 고딕', 12))
            label.pack()
            
        elif answer > x:
            label = Label(win, text='{} Up'.format(x), font=('맑은 고딕', 12))
            label.pack()

        else:
            label = Label(win, text='{} Down'.format(x), font=('맑은 고딕', 12))
            label.pack()

    except :
        label = Label(win, text='1 에서 999 사이의 숫자를 입력하세요.', font=('맑은 고딕', 12))
        label.pack()

    inp.delete(0, END) # 입력창에 입력된 변수 저장 후 입력창에 문자 삭제

def Enter(event):
    try :
        x = int(inp.get())
        if answer == x:
            label = Label(win, text='{} 정답입니다.'.format(x), font=('맑은 고딕', 12))
            label.pack()
        elif answer > x:
            label = Label(win, text='{} Up'.format(x), font=('맑은 고딕', 12))
            label.pack()

        else:
            label = Label(win, text='{} Down'.format(x), font=('맑은 고딕', 12))
            label.pack()
    except :
        label = Label(win, text='1 에서 999 사이의 숫자를 입력하세요.', font=('맑은 고딕', 12))
        label.pack()

    inp.delete(0, END) # 입력창에 입력된 변수 저장후 입력창에 문자 삭제
   
rule = Label(win, text='1 에서 999 사이의 숫자를 입력하세요.'
                , font = ('맑은고딕', 12))
rule.pack()

inp = Entry(win, justify='right') # 입력창, justify='right' 오른쪽 정렬
inp.pack()

btn1 = Button(win, text='Enter', font = ('맑은고딕', 20)) # 버튼
btn1.config(command = UDcode) # 버튼 실행
btn1.pack()

btn2 = Button(win, text='reset', font = ('맑은고딕', 20)) # 리셋버튼
btn2.config(command= reset)
# 위젯파괴?
btn2.pack()

win.bind('<Return>', Enter) # 엔터키 연결

win.mainloop()