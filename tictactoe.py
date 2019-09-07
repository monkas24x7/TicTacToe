import sys
from tkinter import *
import tkinter.messagebox
root = Tk() 
root.title("Tic tac toe")
c=1
play=True
def restart():
    global c
    button1['text']=button2['text']=button3['text']=button4['text']=button5['text']=button6['text']=button7['text']=button8['text']=button9['text']=" "
menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu)   
filemenu.add_command(label='Restart', command=restart) 
filemenu.add_command(label='Exit', command=root.quit) 
helpmenu = Menu(menu)  
def wincon():
    global c
    if ((button1['text']=="X" and button2['text']=="X" and button3['text']=="X")or                     
    (button4['text']=="X" and button5['text']=="X" and button6['text']=="X")or   
    (button7['text']=="X" and button8['text']=="X" and button9['text']=="X")or   
    (button1['text']=="X" and button4['text']=="X" and button7['text']=="X")or   
    (button2['text']=="X" and button5['text']=="X" and button8['text']=="X")or   
    (button3['text']=="X" and button6['text']=="X" and button9['text']=="X")or   
    (button1['text']=="X" and button5['text']=="X" and button9['text']=="X")or   
    (button3['text']=="X" and button5['text']=="X" and button7['text']=="X")):
        tkinter.messagebox.showinfo('X won!')
        c+=1
        buttonreset()   
    elif ((button1['text']=="O" and button2['text']=="O" and button3['text']=="O")or                      
    (button4['text']=="O" and button5['text']=="O" and button6['text']=="O")or   
    (button7['text']=="O" and button8['text']=="O" and button9['text']=="O")or   
    (button1['text']=="O" and button4['text']=="O" and button7['text']=="O")or   
    (button2['text']=="O" and button5['text']=="O" and button8['text']=="O")or   
    (button3['text']=="O" and button6['text']=="O" and button9['text']=="O")or   
    (button1['text']=="O" and button5['text']=="O" and button9['text']=="O")or   
    (button3['text']=="O" and button5['text']=="O" and button7['text']=="O")):
        tkinter.messagebox.showinfo('O won!')
        c+=1
        buttonreset()
    elif button1['text']!=" " and button2['text']!=" " and button3['text']!=" " and button4['text']!=" " and button5['text']!=" " and button6['text']!=" " and button7['text']!=" " and button8['text']!=" " and button9['text']!=" ":
        tkinter.messagebox.showinfo('Its a tie!') 
        c+=1
        buttonreset()          
def ttt(buttons):
    global c
    if buttons['text']==' ' and c%2!=0:
        buttons['text']="X"
        c+=1
        wincon()
    elif  buttons['text']==' ' and c%2==0:
        buttons['text']="O"
        c+=1
        wincon() 
def buttonreset():
    button1['text']=button2['text']=button3['text']=button4['text']=button5['text']=button6['text']=button7['text']=button8['text']=button9['text']=" "
buttons=StringVar()
button1=Button(root,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)
button2=Button(root,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)
button3=Button(root,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)
button4=Button(root,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)
button5=Button(root,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)
button6=Button(root,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)
button7=Button(root,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)
button8=Button(root,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)
button9=Button(root,text=" ",font='Hevetica 20 italic',bg='black',fg='white',height=4,width=8,command=lambda:ttt(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)
root.mainloop()