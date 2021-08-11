#!/usr/bin/env python
# coding: utf-8

# # 계산기 만들기
# ## tkinter 활용

from tkinter import *

win = Tk()

# 변수
temp = '' # 임시저장 변수
output = StringVar() # 출력text
save_list = []

## 함수
# 버튼 클릭 함수
def btn_click(factor):
  global temp
  global save_list
  save_list.append(input_box.get())
  if input_box.get() == '0':
    output.set(str(factor))
  else:
    temp = input_box.get()
    output.set(str(temp) + str(factor))
    
# 클리어 함수
def Clear():
    output.set('0')
    temp=''
    save_list = []

# '=' 버튼 함수
def equal():
  global temp
  global save_list
  save_list.append(input_box.get())
  temp = input_box.get()
  answer = str(eval(temp))
  if answer[-2:] == '.0':  # 소수점 없애기 위한 새로운 방법
    answer = answer.replace('.0', '')
  # fillter(answer)
  output.set(answer)
  temp='' 

# CE 버튼 함수
def CE():
  global temp
  global save_list
  save_list.append(input_box.get())
  temp = input_box.get()
  output.set(temp[:-1])

## 키 입력 함수
def key_input(factor):
  keys = '1234567890/*+-'
  # 키 입력시, btn_click()함수 호출.
  if factor.char in keys :
      btn_click(factor.char)
  # 엔터키 -> =버튼 
  elif factor.keysym == "Return":
      equal()
  # ESC 키 -> AC 버튼 입력.
  elif factor.keysym == "Escape":
      Clear()
    
# 부호 변환 함수 
def switching():
  global temp
  global save_list
  save_list.append(input_box.get())
  temp = input_box.get()
  answer = str(-float(temp))
  if answer[-2:] == '.0':
    answer = answer.replace('.0', '')
  output.set(answer)

# 되돌리기 함수(백스페이스)
def back():
  if save_list != []:
    back = save_list.pop()
    output.set(back)

# 부동소수 필터 함수 --------------- 계속 오류 남
# def fillter():
#   global answer
#   if int(answer) == float(answer):
#     answer = int(answer)
#   else:
#     answer = float(answer)


# 창 기본 설정
win.title('계산기')
win.geometry('248x225')

# 입력창 생성
input_box = Entry(win, justify='right', font=(None, 16, 'bold'), textvariable=output)
output.set(0)
input_box.grid(column=0, row=0, columnspan=4)

output_box = Label(win, justify='right', font=(None, 16, 'bold'), textvariable=output)
output_box.grid(column=4, row=0, columnspan=4)

# 버튼 생성
btn1 = Button(win, text='CE', width=4, height=1, font=(None, 14, 'bold'), command=CE)
btn1.grid(column=0, row=1)

btn2 = Button(win, text='C',width=4, height=1, font=(None, 14, 'bold'), command=Clear)
btn2.grid(column=1, row=1)

btn3 = Button(win, text='undo',width=4, height=1, font=(None, 14, 'bold'), command=back)
btn3.grid(column=2, row=1)

btn4 = Button(win, text='/',width=4, height=1, font=(None, 14, 'bold'), command=lambda: btn_click('/'))
btn4.grid(column=3, row=1)

number_7 = Button(win, text='7',width=4, height=1, font=(None, 14, 'bold'), command=lambda: btn_click(7))
number_7.grid(column=0, row=2)

number_8 = Button(win, text='8',width=4, height=1, font=(None, 14, 'bold'), command=lambda: btn_click(8))
number_8.grid(column=1, row=2)

number_9 = Button(win, text='9',width=4, height=1, font=(None, 14, 'bold'), command=lambda: btn_click(9))
number_9.grid(column=2, row=2)

bnt5 = Button(win, text='X',width=4, height=1, font=(None, 14, 'bold'), command=lambda: btn_click('*'))
bnt5.grid(column=3, row=2)

number_4 = Button(win, text='4',width=4, height=1, font=(None, 14, 'bold'), command=lambda: btn_click(4))
number_4.grid(column=0, row=3)

number_5 = Button(win, text='5',width=4, height=1, font=(None, 14, 'bold'), command=lambda: btn_click(5))
number_5.grid(column=1, row=3)

number_6 = Button(win, text='6',width=4, height=1, font=(None, 14, 'bold'), command=lambda: btn_click(6))
number_6.grid(column=2, row=3)

bnt6 = Button(win, text='-',width=4, height=1, font=(None, 14, 'bold'), command=lambda: btn_click('-'))
bnt6.grid(column=3, row=3)

number_1 = Button(win, text='1',width=4, height=1, font=(None, 14, 'bold'), command=lambda: btn_click(1))
number_1.grid(column=0, row=4)

number_2 = Button(win, text='2',width=4, height=1, font=(None, 14, 'bold'), command=lambda: btn_click(2))
number_2.grid(column=1, row=4)

number_3 = Button(win, text='3',width=4, height=1, font=(None, 14, 'bold'), command=lambda: btn_click(3))
number_3.grid(column=2, row=4)

bnt7 = Button(win, text='+',width=4, height=1, font=(None, 14, 'bold'), command=lambda: btn_click('+'))
bnt7.grid(column=3, row=4)

bnt8 = Button(win, text='+/-',width=4, height=1, font=(None, 14, 'bold'), command=switching)
bnt8.grid(column=0, row=5)

number_0 = Button(win, text='0',width=4, height=1, font=(None, 14, 'bold'), command=lambda: btn_click(0))
number_0.grid(column=1, row=5)

bnt9 = Button(win, text='.',width=4, height=1, font=(None, 14, 'bold'), command=lambda: btn_click('.'))
bnt9.grid(column=2, row=5)

bnt_equal = Button(win, text='=',width=4, height=1, font=(None, 14, 'bold'), command=equal)
bnt_equal.grid(column=3, row=5)

# 키 바인딩
win.bind('<Key>', key_input) # (이벤트 값, 함수) 키 이벤트가 발생하면 key_input 함수에 연결해라

win.mainloop()





