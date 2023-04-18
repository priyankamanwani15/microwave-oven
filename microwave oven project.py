from tkinter import *

root=Tk()
root.geometry('570x260')
root.resizable(width=FALSE, height=FALSE)
'''
widgets are added here
'''
root.title('Microft Microwave')

def start():
    startbtn=Button(root,text='Start',font=('Times New Roman',12,'bold'),borderwidth=3,activebackground='purple',fg='blue',bg='hot pink')
    startbtn.place(x=400,y=220)
start()

def stop():
    stopbtn=Button(root,text='Stop',font=('Times New Roman',12,'bold'),borderwidth=3,activebackground='purple',fg='blue',bg='hot pink')
    stopbtn.place(x=460,y=220)
stop()

def reset():
    resetbtn=Button(root,text='Reset',font=('Times New Roman',12,'bold'),borderwidth=3,activebackground='purple',fg='blue',bg='hot pink')
    resetbtn.place(x=520,y=220)
reset()


lab1=Label(root,bg='black',width=55,height=17)
lab1.place(x=2,y=2)
lab2=Label(root,bg='gray',width=40,height=10)
lab2.place(x=52,y=52)


class numpad:
    def __init__(self,name,x_loc,y_loc,height = 1,width=3,form = root,font=('Times New Roman',12,'bold'),borderwidth=1,activebackground='purple',fg='blue',bg='hot pink'):

        self.btn = Button(form,text = name,height=height,width=width,font=font,borderwidth=borderwidth,activebackground=activebackground,fg=fg,bg=bg)
        self.btn.place(x = x_loc, y = y_loc)
        
btn_1 = numpad('1',430,70)
btn_2 = numpad('2',465,70)
btn_3 = numpad('3',500,70)
btn_4 = numpad('4',430,100)
btn_5 = numpad('5',465,100)
btn_6 = numpad('6',500,100)
btn_7 = numpad('7',430,130)
btn_8 = numpad('8',465,130)
btn_9 = numpad('9',500,130)
btn_0 = numpad('0',465,160)
root.mainloop()