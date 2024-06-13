from tkinter import *
from PIL import ImageTk, Image
import cv2
import playsound as ps
import random
im2 = cv2.imread("E://DATA SCIENCE MINOR-JANUARY//time_over.jpg",1)
frame = Tk()
frame.geometry('400x400')
frame.title('Countdown Timer')
x=0
org=0
stopped=0
def startme():
    global x
    x = int(e1.get())*3600 + int(e2.get())*60 + int(e3.get())+1
    global org
    org = x
    #print(e1.get(),e2.get(),e3.get())
    b4.destroy()
    lab.destroy()
    lb2.destroy()
    lb3.destroy()
    lb4.destroy()
    e1.destroy()
    e2.destroy()
    e3.destroy()
    #stopped=0
    from plyer import notification
    resetted=False
    def printer():
        global x
        global stopped
        if(stopped==0):
            x = x-1
            if(x==0):
                notification.notify(title='alert',message="Times up!",timeout=11)
                #stopped
                stopped = 1
                frame.destroy()
                ps.playsound("E://DATA SCIENCE MINOR-JANUARY//alarm_sound.mp3")
                cv2.imshow("alert",im2)
                return
            val = random.randint(0,7)
            colors=['red','magenta','green','pink','aqua','orange','white','cyan']
            cs = colors[val]
            lb.config(text = represent(x),fg=cs)
            lb.after(1000,printer)
        if(resetted==True):
            val = random.randint(0,7)
            colors=['red','magenta','green','pink','aqua','orange','white','cyan']
            cs = colors[val]
            lb.config(text = represent(x),fg=cs)
            lb.after(1000,printer)
    def stop():
        global stopped
        stopped = 1
        global resetted
        resetted = False
        #print("Hello")
    def start():
        global stopped
        stopped = 0
        global resetted
        resetted = False
        printer()
    def reset():
        val = random.randint(0,7)
        colors=['red','magenta','green','pink','aqua','orange','white','cyan']
        cs = colors[val]
        lb.config(text=represent(org),fg=cs)
        global x
        x = org
        global stopped
        stopped = 1
        global resetted
        resetted = True
        printer()
    def shoon():
        frame.destroy()
        import minor_project_timer
    def represent(P):
        hrs = P//3600
        if(hrs<10):
            hrs = "0"+str(hrs)
        else:
            hrs = str(hrs)
        mts = (P%3600)//60
        if(mts<10):
            mts = "0"+str(mts)
        else:
            mts = str(mts)
        sec = (P%3600)%60
        if(sec<10):
            sec = "0"+str(sec)
        else:
            sec = str(sec)
        return hrs+":"+mts+":"+sec
    lb = Label(frame,font=("Times New Roman",30),bg="Black")
    lb.pack()
    l3=Label(frame,text="")
    l3.pack()
    l4 = Label(frame,text="")
    l4.pack()
    bt = Button(frame,text="Stop",command = stop,fg="yellow",bg="Black",font=("Times New Roman",20))
    bt.pack()
    bt2 = Button(frame,text="Resume",command = start,fg="yellow",bg="Black",font=("Times New Roman",20))
    bt2.pack()
    bt3 = Button(frame,text = "Reset",command = reset,fg="yellow",bg="Black",font=("Times New Roman",20))
    bt3.pack()
    bt4 = Button(frame,text="Start New Timer",command = shoon,fg="yellow",bg="Black",font=("Times New Roman",20))
    bt4.pack()
    printer()
    #window.mainloop()
    #print("Hello")
background = ImageTk.PhotoImage(Image.open("E://DATA SCIENCE MINOR-JANUARY//AR.jpg"))
lab = Label(frame,image = background)
lb2 = Label(frame,text="Hours")
lb3 = Label(frame,text="Minutes")
lb4 = Label(frame,text="Seconds")
e1 = Entry(frame,width=4)
e2 = Entry(frame,width=4)
e3 = Entry(frame,width=4)
lab.pack()
lb2.pack()
e1.pack()
lb3.pack()
e2.pack()
lb4.pack()
e3.pack()
lap = Label(frame,image = ImageTk.PhotoImage(Image.open("E://DATA SCIENCE MINOR-JANUARY//AR.jpg")))
b4 = Button(frame,text = "Start",width=7,command = startme,borderwidth=0,fg="yellow",bg="black")
b4.pack()
mainloop()
