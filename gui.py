from tkinter import *
class App:
    algorithms = [
    ("Hill Climbing", 1),
    ("First Choice Hill Climbing", 2),
    ("Random Restart or Parallel Hill Climbing", 3),
    ("Simulated Annealing", 4),
    ("Local Beam Search", 5)]
    def __init__(self, master):
        v = IntVar()
        v.set(1)
        frame = Frame(master)
        frame.pack()
        Label(text="Choose a search algorithm: ").pack()
        for txt, val in self.algorithms:
            Radiobutton(root, text=txt, value=val, variable=v).pack(anchor=W)
        self.button_quit = Button(text="Quit", command=frame.quit)
        self.button_quit.pack(side=LEFT)
        self.button_execute = Button(text="Execute search", command=self.execute(v))
        self.button_execute.pack(side=LEFT)

    def execute(self, v):
        print(v.get())

root = Tk()
app = App(root)
root.mainloop()
