import tkinter
from tkinter import messagebox
import os
import sys
import subprocess
#from playsound import playsound

x_o = True
flag = 0

def tictactoe():
    def bclick(button):
        global x_o, flag
        button["bg"] = "#2ec4b6"
        if button["text"] == "" and x_o:
            print(flag)
            button["text"] = "X"
            x_o = False
            winCon()
            flag += 1
        elif button["text"] == "" and not x_o:
            print(flag)
            button["text"] = "O"
            x_o = True
            winCon()
            flag += 1
        else:
            messagebox.showinfo("Tic-Tac-Toe", "Space already occupied.")

    def winCon():
        if flag == 8:
            messagebox.showinfo("Tic-Tac-Toe", "Tie game!")
            main.destroy()
        elif b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" or \
             b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" or \
             b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" or \
             b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" or \
             b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X" or \
             b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" or \
             b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" or \
             b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            #playsound("C:\\Users\\lucas\\source\\repos\\Tic Tac Toe\\Tic Tac Toe\\win31.mp3")
            messagebox.showinfo("Tic-Tac-Toe", "X wins!")
            main.destroy()
        elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" or \
             b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" or \
             b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" or \
             b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" or \
             b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O" or \
             b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" or \
             b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" or \
             b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            #playsound("C:\\Users\\lucas\\source\\repos\\Tic Tac Toe\\Tic Tac Toe\\win31.mp3")
            messagebox.showinfo("Tic-Tac-Toe", "O wins!")
            main.destroy()      

    def temp():
        x_o = True
        flag = 0
        main.destroy()
        temp2()
        #subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])


    main = tkinter.Tk()
    main.title("Tic-Tac-Toe")
    global b1, b2, b3, b4, b5, b6, b7, b8, b9

    b1 = tkinter.Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: bclick(b1))
    b1.grid(row=0, column=0)

    b2 = tkinter.Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: bclick(b2))
    b2.grid(row=0, column=1)

    b3 = tkinter.Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: bclick(b3))
    b3.grid(row=0, column=2)

    b4 = tkinter.Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: bclick(b4))
    b4.grid(row=1, column=0)

    b5 = tkinter.Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: bclick(b5))
    b5.grid(row=1, column=1)

    b6 = tkinter.Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: bclick(b6))
    b6.grid(row=1, column=2)

    b7 = tkinter.Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: bclick(b7))
    b7.grid(row=2, column=0)

    b8 = tkinter.Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: bclick(b8))
    b8.grid(row=2, column=1)

    b9 = tkinter.Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: bclick(b9))
    b9.grid(row=2, column=2)

    #b10 = tkinter.Button(main, text="Clear", command=lambda: temp())
    #b10.grid(row=3, column=0)

    b11 = tkinter.Button(main, text="Exit", command=main.destroy)
    b11.grid(row=3, column=1)

    main.mainloop()

tictactoe()
