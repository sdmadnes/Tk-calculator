from tkinter import *

root = Tk()
root.title('TK - сука')

root.iconbitmap('')

root.geometry('385x590+-10+0')
root.resizable(False,False)
root.config(bg='grey')
primer = '0'

def add(num):
    global primer,a
    if L['text'] == '0' or a == True:
        a = False
        L['text'] = num
        primer = num
    else:
        L['text'] += num
        if num == 'x':
            num = '*'
        primer += num
    print(L['text'])

def eval_():
    global primer,a
    s = primer
    L['text'] = eval(s)
    a = True
    primer = '0'




#GridButtons
L = Label(root, text = '0',borderwidth=80)
L.pack(fill=X)

GB = Frame(root)
GB.pack(fill=X)

btn7 = Button(GB, text='7',padx=40,pady=40, command=lambda: add('7')).grid(row=0,column=0)
btn8 = Button(GB, text='8',padx=40,pady=40, command=lambda: add('8')).grid(row=0,column=1)
btn9 = Button(GB, text='9',padx=40,pady=40, command=lambda: add('8')).grid(row=0,column=2)
btn9 = Button(GB, text='+',padx=40,pady=40, command=lambda: add('+')).grid(row=0,column=3)

btn4 = Button(GB, text='4',padx=40,pady=40, command=lambda: add('4')).grid(row=1,column=0)
btn5 = Button(GB, text='5',padx=40,pady=40, command=lambda: add('5')).grid(row=1,column=1)
btn6 = Button(GB, text='6',padx=40,pady=40, command=lambda: add('6')).grid(row=1,column=2)
btn9 = Button(GB, text='-',padx=40,pady=40, command=lambda: add('-')).grid(row=1,column=3)

btn1 = Button(GB, text='1',padx=40,pady=40, command=lambda: add('1')).grid(row=2,column=0)
btn2 = Button(GB, text='2',padx=40,pady=40, command=lambda: add('2')).grid(row=2,column=1)
btn3 = Button(GB, text='3',padx=40,pady=40, command=lambda: add('3')).grid(row=2,column=2)
btn9 = Button(GB, text='x',padx=40,pady=40, command=lambda: add('x')).grid(row=2,column=3)

btn_tochka = Button(GB,text='.',padx=40,pady=40, command=lambda: add('.')).grid(row=3,column=0)
btn0 = Button(GB, text='0',padx=40,pady=40, command=lambda: add('0')).grid(row=3,column=1)
btn00 = Button(GB, text='00',padx=40,pady=40, command=lambda: add('00')).grid(row=3,column=2)
eval_input = Button(GB, text='=',padx=40,pady=40,command=eval_).grid(row=3,column=3)
