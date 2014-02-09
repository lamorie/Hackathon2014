from tkinter import *
import turtle 

root = Tk()

turtle.shape("turtle")

def moveForward():
    turtle.forward(100)
def moveBackward():
    turtle.backward(100)
def moveLeft():
    turtle.left(90)
def moveRight():
    turtle.right(90)
def moveCircle():
    turtle.circle(50)
def moveStamp():
    turtle.stamp()
def movePenUp():
    turtle.penup()
def movePenDown():
    turtle.pendown()
def moveColor():
    turtle.color("red", "teal", "blue")
def moveClear():
    turtle.clear()
    
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
def dispCircle():
    r = Label(dispFrame, text = "turtle.circle(50)")
    r.pack()
    cmdList.append(moveCircle);
def dispStamp():
    r = Label(dispFrame, text = "turtle.stamp()")
    r.pack()
    cmdList.append(moveStamp);
def dispPenUp():
    r = Label(dispFrame, text = "turtle.penup()")
    r.pack()
    cmdList.append(movePenUp);
def dispPenDown():
    r = Label(dispFrame, text = "turtle.pendown()")
    r.pack()
    cmdList.append(movePenDown);
def dispColor():
    r = Label(dispFrame, text = "turtle.color(\"red\", \"teal\", \"blue\")")
    r.pack()
    cmdList.append(moveColor);
def dispClear():
    r = Label(dispFrame, text = "turtle.clear()")
    r.pack()
    cmdList.append(moveClear);
    
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
circle = Button(cmdFrame, text="Circle", command=dispCircle)
circle.pack(side=TOP)
circle.grid(row = 4, column = 0)
stamp = Button(cmdFrame, text="Stamp", command=dispStamp)
stamp.pack(side=TOP)
stamp.grid(row = 5, column = 0)
penUp = Button(cmdFrame, text="Pen Up", command=dispPenUp)
penUp.pack(side=TOP)
penUp.grid(row = 6, column = 0)
penDown = Button(cmdFrame, text="Pen Up", command=dispPenDown)
penDown.pack(side=TOP)
penDown.grid(row = 7, column = 0)
color = Button(cmdFrame, text="Color", command=dispColor)
color.pack(side=TOP)
color.grid(row = 8, column = 0)
clear = Button(cmdFrame, text="Clear", command=dispClear)
clear.pack(side=TOP)
clear.grid(row = 9, column = 0)

execute = Button(cmdFrame, text="Execute", command=run)
execute.pack(side=BOTTOM)
execute.grid(row = 10, column = 0)

root.geometry("600x500+0+0")
root.mainloop()  
