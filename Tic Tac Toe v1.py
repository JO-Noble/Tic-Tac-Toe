from tkinter import *
import os

window = Tk()
window.title("Tic Tac Toe")
window.minsize(400,200)
window.configure(background=("black"))

global T
T = 1


def change_player():
    print("turn_chnager")

    global T

    if T == 2:
        T -= 1
        print("too 1")
    elif T == 1:
        T += 1
        print("too 2")
    else:
        print("error")

def check_win():
    if button1["text"] == "X" and button2['text'] == 'X' and button3['text'] == 'X':
       print("X wins")
       button11.configure(text='X wins')
    elif button1["text"] == "O" and button2['text'] == 'O' and button3['text'] == 'O':
       print("O wins")
       button11.configure(text='O wins')
       
    elif button4["text"] == "X" and button5['text'] == 'X' and button6['text'] == 'X':
       print("X wins")
       button11.configure(text='X wins')
    elif button4["text"] == "O" and button5['text'] == 'O' and button6['text'] == 'O':
       print("O wins")
       button11.configure(text='O wins')
       
    elif button7["text"] == "X" and button8['text'] == 'X' and button9['text'] == 'X':
       print("O wins")
       button11.configure(text='X wins')
    elif button7["text"] == "O" and button8['text'] == 'O' and button9['text'] == 'O':
       print("O wins")
       button11.configure(text='O wins')
       
    elif button1["text"] == "X" and button4['text'] == 'X' and button7['text'] == 'X':
       print("X wins")
       button11.configure(text='X wins')
    elif button1["text"] == "O" and button4['text'] == 'O' and button7['text'] == 'O':
       print("O wins")
       button11.configure(text='O wins')
       
    elif button2["text"] == "X" and button5['text'] == 'X' and button8['text'] == 'X':
       print("X wins")
       button11.configure(text='X wins')
    elif button2["text"] == "O" and button5['text'] == 'O' and button8['text'] == 'O':
       print("O wins")
       button11.configure(text='O wins')
       
    elif button3["text"] == "X" and button6['text'] == 'X' and button9['text'] == 'X':
       print("X wins")
       button11.configure(text='X wins')
    elif button3["text"] == "O" and button6['text'] == 'O' and button9['text'] == 'O':
       print("O wins")
       button11.configure(text='O wins')
       
    elif button1["text"] == "X" and button5['text'] == 'X' and button9['text'] == 'X':
       print("X wins")
       button11.configure(text='X wins')
    elif button1["text"] == "O" and button5['text'] == 'O' and button9['text'] == 'O':
       print("O wins")
       button11.configure(text='O wins')
       
    elif button3["text"] == "X" and button5['text'] == 'X' and button7['text'] == 'X':
       print("X wins")
       button11.configure(text='X wins')
    elif button3["text"] == "O" and button5['text'] == 'O' and button7['text'] == 'O':
       print("O wins")
       button11.configure(text='O wins')
    

def reset():
    button1.configure(text='')
    button2.configure(text='')
    button3.configure(text='')
    button4.configure(text='')
    button5.configure(text='')
    button6.configure(text='')
    button7.configure(text='')
    button8.configure(text='')
    button9.configure(text='')
    button11.configure(text='')
    global T
    T = 1
    print("hope")
    #window.destroy()
    #exit()


def activate_1():
    if button1["text"] == "":
       print("text_detection")
       if T == 1:
          button1.configure(text="X")
          print("X")
          change_player()
          check_win()
         

       elif T == 2:
            button1.configure(text="O")
            print("O")
            change_player()
            check_win()
       else:
            print("error")


def activate_2():
    if button2["text"] == "":
       print("text_detection")
       if T == 1:
          button2.configure(text="X")
          print("X")
          change_player()
          check_win()

       elif T == 2:
            button2.configure(text="O")
            print("O")
            change_player()
            check_win()
       else:
            print("error")


def activate_3():
    if button3["text"] == "":
       print("text_detection")
       if T == 1:
          button3.configure(text="X")
          print("X")
          change_player()
          check_win()

       elif T == 2:
          button3.configure(text="O")
          print("O")
          change_player()
          check_win()
       else:
          print("error")


def activate_4():
    if button4["text"] == "":
       print("text_detection")
       if T == 1:
          button4.configure(text="X")
          print("X")
          change_player()
          check_win()

       elif T == 2:
          button4.configure(text="O")
          print("O")
          change_player()
          check_win()
       else:
          print("error")


def activate_5():
    if button5["text"] == "":
       print("text_detection")
       if T == 1:
          button5.configure(text="X")
          print("X")
          change_player()
          check_win()

       elif T == 2:
          button5.configure(text="O")
          print("O")
          change_player()
          check_win()
       else:
          print("error")


def activate_6():
    if button6["text"] == "":
       print("text_detection")
       if T == 1:
          button6.configure(text="X")
          print("X")
          change_player()
          check_win()

       elif T == 2:
          button6.configure(text="O")
          print("O")
          change_player()
          check_win()
       else:
          print("error")


def activate_7():
    if button7["text"] == "":
       print("text_detection")
       if T == 1:
          button7.configure(text="X")
          print("X")
          change_player()
          check_win()

       elif T == 2:
          button7.configure(text="O")
          print("O")
          change_player()
          check_win()
       else:
          print("error")


def activate_8():
    if button8["text"] == "":
       print("text_detection")
       if T == 1:
          button8.configure(text="X")
          print("X")
          change_player()
          check_win()

       elif T == 2:
          button8.configure(text="O")
          print("O")
          change_player()
          check_win()
       else:
          print("error")


def activate_9():
    if button9["text"] == "":
       print("text_detection")
       if T == 1:
          button9.configure(text="X")
          print("X")
          change_player()
          check_win()

       elif T == 2:
          button9.configure(text="O")
          print("O")
          change_player()
          check_win()
       else:
          print("error")




button1 = Button(window,text="", fg="white", bg="grey",
                command=activate_1, height=4, width=12)
button1.grid(row=0, column=0)


button2 = Button(window,text="", fg="white", bg="grey",
                command=activate_2, height=4, width=12)
button2.grid(row=0, column=2)


button3 = Button(window,text="", fg="white", bg="grey",
                command=activate_3, height=4, width=12)
button3.grid(row=0, column=4)


button4 = Button(window,text="", fg="white", bg="grey",
                command=activate_4, height=4, width=12)
button4.grid(row=2, column=0)


button5 = Button(window,text="", fg="white", bg="grey",
                command=activate_5, height=4, width=12)
button5.grid(row=2, column=2)


button6 = Button(window,text="", fg="white", bg="grey",
                command=activate_6, height=4, width=12)
button6.grid(row=2, column=4)


button7 = Button(window,text="", fg="white", bg="grey",
                command=activate_7, height=4, width=12)
button7.grid(row=4, column=0)


button8 = Button(window,text="", fg="white", bg="grey",
                command=activate_8, height=4, width=12)
button8.grid(row=4, column=2)


button9 = Button(window,text="", fg="white", bg="grey",
                command=activate_9, height=4, width=12)
button9.grid(row=4, column=4)


button10 = Button(window,text="Reset", fg="white", bg="grey",
                command=reset, height=4, width=12)
button10.grid(row=8, column=8)


button11 = Button(window,text='', fg='white', bg='grey',
                 height=2, width=12)
button11.grid(row=8, column=2)


window.mainloop()
