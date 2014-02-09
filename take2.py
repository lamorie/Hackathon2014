import tkinter as tk
from tkinter import *
from tkinter import ttk
import turtle


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        #self._geom='200x200+0+0'
        #master.geometry("{0}x{1}+0+0".format(
            #master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
       
        tab=ttk.Notebook(master)
        tab.pack(side = 'left', anchor = 'nw', fill = 'y', expand= 'yes')
        pg1 = tk.Frame(bg = 'deep pink')
        pg2 = tk.Frame(bg = 'purple')
        tab.add(pg1, text= 'MOVE')
        tab.add(pg2, text= 'STYLE')
        self.moves(pg1, master)
        self.style(pg2, master)
        
        execute = tk.Button(root, text="Execute", command= lambda: self.run(), bg = 'lime green', padx = 10, pady = 10)
        execute.pack(side='bottom')
        
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

    def moves(self, pg1, master):
        forward = tk.Button(pg1, text="Forward", command= lambda: self.dispForward(master))
        forward.pack(side='top', anchor='nw', padx=50, pady=5)
        
        backward = tk.Button(pg1, text="Backward", command= lambda: self.dispBackward(master))
        backward.pack(side='top', anchor='nw', padx=50, pady=5)
        
        left = tk.Button(pg1, text="Left", command= lambda: self.dispLeft(master))
        left.pack(side='top', anchor='nw', padx=50, pady=5)

        right = tk.Button(pg1, text="Right", command= lambda: self.dispRight(master))
        right.pack(side='top', anchor='nw', padx=50, pady=5)

        circle = tk.Button(pg1, text="Circle", command= lambda: self.dispCircle(master))
        circle.pack(side='top', anchor='nw', padx=50, pady=5)

        goto = tk.Button(pg1, text='Goto', command = lambda: self.dispGoto(master))
        goto.pack(side = 'top', anchor = 'nw', padx = 50, pady = 5)


    def style(self, pg2, master):
        stamp = Button(pg2, text="Stamp", command= lambda: self.dispStamp(master))
        stamp.pack(side='top', anchor='nw', padx=50, pady=5)

        penUp = Button(pg2, text="Pen Up", command= lambda: self.dispPenUp(master))
        penUp.pack(side='top', anchor='nw', padx=50, pady=5)

        penDown = Button(pg2, text="Pen Down", command= lambda: self.dispPenDown(master))
        penDown.pack(side='top', anchor='nw', padx=50, pady=5)

        color = Button(pg2, text="Color", command= lambda: self.dispColor(master))
        color.pack(side='top', anchor='nw', padx=50, pady=5)

        clear = Button(pg2, text="Clear", command= lambda: self.dispClear(master))
        clear.pack(side='top', anchor='nw', padx=50, pady=5)


        
    def moveForward(self):
        turtle.forward(100)
    def moveBackward(self):
        turtle.backward(100)
    def moveLeft(self):
        turtle.left(90)
    def moveRight(self):
        turtle.right(90)
    def moveCircle(self):
        turtle.circle(50)
    def moveGoto(self):
        turtle.goto(0, 0)
    def StyStamp(self):
        turtle.stamp()
    def StyPenUp(self):
        turtle.penup()
    def StyPenDown(self):
        turtle.pendown()
    def StyColor(self):
        turtle.color("green")
    def StyClear(self):
        turtle.clear()
    
    def run(self):
        for func in cmdList:
            func()

    def dispForward(self, master):
        fwd = Label(master, text = "turtle.forward(100)")
        fwd.pack(side='top', anchor = 'nw')
        cmdList.append(self.moveForward);
        

    def dispBackward(self, master):
        bkwd = Label(master, text = "turtle.backward(100)")
        bkwd.pack()
        cmdList.append(self.moveBackward);
        
    def dispLeft(self, master):
        l = Label(master, text = "turtle.left(90)")
        l.pack()
        cmdList.append(self.moveLeft);
        
    def dispRight(self, master):
        r = Label(master, text = "turtle.right(90)")
        r.pack()
        cmdList.append(self.moveRight);
        
    def dispCircle(self, master):
        r = Label(master, text = "turtle.circle(50)")
        r.pack()
        cmdList.append(self.moveCircle);

    def dispGoto(self, master):
        r = Label(master, text = "turtle.goto('center')")
        r.pack()
        cmdList.append(self.moveGoto);
        
    def dispStamp(self, master):
        r = Label(master, text = "turtle.stamp()")
        r.pack()
        cmdList.append(self.StyStamp);
    def dispPenUp(self, master):
        r = Label(master, text = "turtle.penup()")
        r.pack()
        cmdList.append(self.StyPenUp);
    def dispPenDown(self, master):
        r = Label(master, text = "turtle.pendown()")
        r.pack()
        cmdList.append(self.StyPenDown);
    def dispColor(self, master):
        r = Label(master, text = """turtle.color('green')""")
        r.pack()
        cmdList.append(self.StyColor);
    def dispClear(self, master):
        r = Label(master, text = "turtle.clear()")
        r.pack()
        cmdList.append(lambda: self.StyClear());
        

root=tk.Tk()
root["bg"] = "white"
turtle.shape("turtle")
cmdList = []

app=FullScreenApp(root)
root.mainloop()
