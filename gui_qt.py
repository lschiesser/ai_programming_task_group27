import sys
from PyQt5.QtWidgets import *

class App(QWidget):
    algorithms = [
    ("Hill Climbing", 1),
    ("First Choice Hill Climbing", 2),
    ("Random Restart or Parallel Hill Climbing", 3),
    ("Simulated Annealing", 4),
    ("Local Beam Search", 5)]
    algorithm_chosen = 0
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Programming Task")

        layout = QGridLayout()
        self.setLayout(layout)

        #create buttongroup to group radiobuttons together
        self.buttongroup = QButtonGroup()
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)

        #create for every possible search algorithm a radiobutton and add it to
        #the created buttongroup
        for txt, val in self.algorithms:
            radiobutton = QRadioButton(txt)
            radiobutton.algorithm = val
            self.buttongroup.addButton(radiobutton, val)
            layout.addWidget(radiobutton)

        button_execute = QPushButton("Execute search")
        button_execute.clicked.connect(self.execute)
        layout.addWidget(button_execute, 5, 0)

        button_quit = QPushButton("Quit")
        button_quit.clicked.connect(self.quit)
        layout.addWidget(button_quit, 5, 1)

    def execute(self):
        print("Click")

    def quit(self):
        sys.exit()

    def on_button_clicked(self, id):
        """
        checks which of the radiobutton is checked and stores it in a variable
        """
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                algorithm_chosen = button.algorithm
                print(algorithm_chosen)

app = QApplication(sys.argv)
screen = App()
screen.show()
sys.exit(app.exec_())
