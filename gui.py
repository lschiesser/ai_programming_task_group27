from tkinter import *
class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button_quit = Button(text="Quit", command=frame.quit)
        self.button_quit.pack(side=LEFT)
        self.button_execute = Button(text="Execute search", command=self.execute)
        self.button_execute.pack(side=LEFT)

    def execute(self):
        print("Hi")

root = Tk()
app = App(root)
root.mainloop()
