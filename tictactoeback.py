from tkinter import *
import tkinter.messagebox
tk = Tk() 
tk.title("Tic tac toe")
click=True
count=0
def buttonreset():
    button1['text']=button2['text']=button3['text']=button4['text']=button5['text']=button6['text']=button7['text']=button8['text']=button9['text']=" "
def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)
def wincon():
    if count==8:
        disableButton()
        tkinter.messagebox.showinfo('Its a tie')
        buttonreset()
    elif button1['text']=="X" and button2['text']=="X" and button3['text']=="X":
        disableButton()
        tkinter.messagebox.showinfo("X won!")
        buttonreset()                   
    elif button4['text']=="X" and button5['text']=="X" and button6['text']=="X":
        disableButton()
        tkinter.messagebox.showinfo("X won!")
        buttonreset()
    elif button7['text']=="X" and button8['text']=="X" and button9['text']=="X":
        disableButton()
        tkinter.messagebox.showinfo("X won!")
        buttonreset()
    elif button1['text']=="X" and button4['text']=="X" and button7['text']=="X":
        disableButton()
        tkinter.messagebox.showinfo("X won!")
        buttonreset()
    elif button2['text']=="X" and button5['text']=="X" and button8['text']=="X":
        disableButton()
        tkinter.messagebox.showinfo("X won!")
        buttonreset()
    elif button3['text']=="X" and button6['text']=="X" and button9['text']=="X":
        disableButton()
        tkinter.messagebox.showinfo("X won!")
        buttonreset()
    elif button1['text']=="X" and button5['text']=="X" and button9['text']=="X":
        disableButton()
        tkinter.messagebox.showinfo("X won!")
        buttonreset()
    elif button3['text']=="X" and button5['text']=="X" and button7['text']=="X":
        disableButton()
        tkinter.messagebox.showinfo("X won!")
        buttonreset()
    elif button1['text']=="O" and button2['text']=="O" and button3['text']=="O":
        disableButton()
        tkinter.messagebox.showinfo("O won!")
        buttonreset()                   
    elif button4['text']=="O" and button5['text']=="O" and button6['text']=="O":
        disableButton()
        tkinter.messagebox.showinfo("O won!")
        buttonreset()
    elif button7['text']=="O" and button8['text']=="O" and button9['text']=="O":
        disableButton()
        tkinter.messagebox.showinfo("O won!")
        buttonreset()
    elif button1['text']=="O" and button4['text']=="O" and button7['text']=="O":
        disableButton()
        tkinter.messagebox.showinfo("O won!")
        buttonreset()
    elif button2['text']=="O" and button5['text']=="O" and button8['text']=="O":
        disableButton()
        tkinter.messagebox.showinfo("O won!")
        buttonreset()
    elif button3['text']=="O" and button6['text']=="O" and button9['text']=="O":
        disableButton()
        tkinter.messagebox.showinfo("O won!")
        buttonreset()
    elif button1['text']=="O" and button5['text']=="O" and button9['text']=="O":
        disableButton()
        tkinter.messagebox.showinfo("O won!")
        buttonreset()
    elif button3['text']=="O" and button5['text']=="O" and button7['text']=="O":
        disableButton()
        tkinter.messagebox.showinfo("O won!")
        buttonreset()
def ttt(buttons):
    global click,count
    if buttons['text']==' ' and click==True:
        buttons['text']="X"
        click=False
        wincon()
        count+=1
    elif  buttons['text']==' ' and click==False:
        buttons['text']="O"
        click=True
        wincon()
        count+=1  
buttons=StringVar()
button1=Button(tk,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)
button2=Button(tk,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)
button3=Button(tk,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)
button4=Button(tk,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)
button5=Button(tk,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)
button6=Button(tk,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)
button7=Button(tk,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)
button8=Button(tk,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)
button9=Button(tk,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)
tk.mainloop()