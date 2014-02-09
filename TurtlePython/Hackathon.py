from tkinter import *
import turtle 

root = Tk()

def moveForward():
    turtle.forward(100)
def moveBackward():
    turtle.backward(100)
def moveLeft():
    turtle.left(90)
def moveRight():
    turtle.right(90)
def run():
    for func in cmdList:
        func()
    
def dispForward():
    fwd = Label(dispFrame, text = "turtle.forward(100)")
    fwd.pack()
    cmdList.append(moveForward);
    cmdList
def dispBackward():
    bkwd = Label(dispFrame, text = "turtle.backward(100)")
    bkwd.pack()
    cmdList.append(moveBackward);
def dispLeft():
    l = Label(dispFrame, text = "turtle.left(90)")
    l.pack()
    cmdList.append(moveLeft);
def dispRight():
    r = Label(dispFrame, text = "turtle.right(90)")
    r.pack()
    cmdList.append(moveRight);

cmdList = []

cmdFrame = Frame(root)
cmdFrame.pack( side = LEFT )
dispFrame = Frame(root)
dispFrame.pack( side = RIGHT )

forward = Button(cmdFrame, text="Forward", command=dispForward)
forward.pack(side=TOP)
forward.grid(row = 0, column = 0)
backward = Button(cmdFrame, text="Backward", command=dispBackward)
backward.pack(side=TOP)
backward.grid(row = 1, column = 0)
left = Button(cmdFrame, text="Left", command=dispLeft)
left.pack(side=TOP)
left.grid(row = 2, column = 0)
right = Button(cmdFrame, text="Right", command=dispRight)
right.pack(side=TOP)
right.grid(row = 3, column = 0)

execute = Button(cmdFrame, text="Execute", command=run)
execute.pack(side=BOTTOM)
execute.grid(row = 4, column = 0)

root.geometry("600x500+0+0")
root.mainloop()  
