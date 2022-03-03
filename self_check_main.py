from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Grid Manager")

        for r in range(6):
            self.master.rowconfigure(r, weight=1)
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
            Button(master, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)

        Frame1 = Frame(master, bg="red")
        Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)
        Frame2 = Frame(master, bg="blue")
        Frame2.grid(row = 3, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)
        Frame3 = Frame(master, bg="green")
        Frame3.grid(row = 0, column = 2, rowspan = 6, columnspan = 3, sticky = W+E+N+S)

class Application1(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Grid Manager")

        for r in range(10):
            self.master.rowconfigure(r, weight=1)
        for c in range(6):
            self.master.columnconfigure(c, weight=1)
            #Button(master, text="Button {0}".format(c)).grid(row=6,column=c,sticky=E+W)

        Frame1 = Frame(master, bg="grey")
        Frame1.grid(row = 0, column = 0, rowspan = 10, columnspan = 6, sticky = W+E+N+S)

        Frame2 = Frame(master, bg="white")
        Frame2.grid(row = 2, column = 0, rowspan = 10, columnspan = 6, sticky = W+E+N+S)

        label1 = Label(Frame2, text="XXXXXXXX", font='Arial 12 bold')
        label1.place(relx=0.5, rely=0.5, anchor=CENTER)

        label2 = Label(Frame2, text="I am inside a Frame", font='Arial 17 bold')
        label2.place(relx=0.5, rely=0.5, anchor=CENTER)

        #Frame3 = Frame(master, bg="green")
        #Frame3.grid(row = 0, column = 2, rowspan = 6, columnspan = 3, sticky = W+E+N+S)

root = Tk()
root.attributes("-fullscreen", True)
root.bind("<F11>", lambda event: root.attributes("-fullscreen",not root.attributes("-fullscreen")))
#root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
app = Application1(master=root)
app.mainloop()