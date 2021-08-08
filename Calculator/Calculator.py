#!/usr/bin/env python
# coding: utf-8

# # 계산기 만들기
# ## tkinter 활용

from tkinter import *

win = Tk()

# 함수

 ## 숫자 클릭
def number_click(number):
    temp = input_box.get()
    input_box.delete(0, END)
    result = str(temp) + str(number) # 입력창을 띄울 때 0을 넣고 싶었는데 그렇게 하면 버튼을 누르면 0이 맨 앞으로 오더라
    input_box.insert(0, int(result)) # 그게 싫어서 int형으로 뿌려버림

 ## 버튼 클릭
  ### 클리어
def Clear():
    input_box.delete(0, END)

  ### 더하기

    


# 창 기본 설정
win.title('계산기')
win.geometry('248x225')

# 입력창 생성
input_box = Entry(win, justify='right', font=(None, 16, 'bold'))
input_box.insert(0, "0")
input_box.grid(column=0, row=0, columnspan=4)

# 버튼 생성
btn1 = Button(win, text='CE', width=4, height=1, font=(None, 14, 'bold'), command='###')
btn1.grid(column=0, row=1)

btn2 = Button(win, text='C',width=4, height=1, font=(None, 14, 'bold'), command='###')
btn2.grid(column=1, row=1)

btn3 = Button(win, text='<-',width=4, height=1, font=(None, 14, 'bold'), command='###')
btn3.grid(column=2, row=1)

btn4 = Button(win, text='%',width=4, height=1, font=(None, 14, 'bold'), command='###')
btn4.grid(column=3, row=1)

number_7 = Button(win, text='7',width=4, height=1, font=(None, 14, 'bold'), command=lambda: number_click(7))
number_7.grid(column=0, row=2)

number_8 = Button(win, text='8',width=4, height=1, font=(None, 14, 'bold'), command=lambda: number_click(8))
number_8.grid(column=1, row=2)

number_9 = Button(win, text='9',width=4, height=1, font=(None, 14, 'bold'), command=lambda: number_click(9))
number_9.grid(column=2, row=2)

bnt5 = Button(win, text='X',width=4, height=1, font=(None, 14, 'bold'), command='###')
bnt5.grid(column=3, row=2)

number_4 = Button(win, text='4',width=4, height=1, font=(None, 14, 'bold'), command=lambda: number_click(4))
number_4.grid(column=0, row=3)

number_5 = Button(win, text='5',width=4, height=1, font=(None, 14, 'bold'), command=lambda: number_click(5))
number_5.grid(column=1, row=3)

number_6 = Button(win, text='6',width=4, height=1, font=(None, 14, 'bold'), command=lambda: number_click(6))
number_6.grid(column=2, row=3)

bnt6 = Button(win, text='-',width=4, height=1, font=(None, 14, 'bold'), command='###')
bnt6.grid(column=3, row=3)

number_1 = Button(win, text='1',width=4, height=1, font=(None, 14, 'bold'), command=lambda: number_click(1))
number_1.grid(column=0, row=4)

number_2 = Button(win, text='2',width=4, height=1, font=(None, 14, 'bold'), command=lambda: number_click(2))
number_2.grid(column=1, row=4)

number_3 = Button(win, text='3',width=4, height=1, font=(None, 14, 'bold'), command=lambda: number_click(3))
number_3.grid(column=2, row=4)

bnt7 = Button(win, text='+',width=4, height=1, font=(None, 14, 'bold'), command='###')
bnt7.grid(column=3, row=4)

bnt8 = Button(win, text='+/-',width=4, height=1, font=(None, 14, 'bold'), command='###')
bnt8.grid(column=0, row=5)

number_0 = Button(win, text='0',width=4, height=1, font=(None, 14, 'bold'), command='###')
number_0.grid(column=1, row=5)

bnt9 = Button(win, text='.',width=4, height=1, font=(None, 14, 'bold'), command='###')
bnt9.grid(column=2, row=5)

bnt_equal = Button(win, text='=',width=4, height=1, font=(None, 14, 'bold'), command='###')
bnt_equal.grid(column=3, row=5)



win.mainloop()





