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
        label_warehouse = QLabel()
        label_warehouse.setText("Pick data to set up warehouse")
        layout.addWidget(label_warehouse, 0, 0)

        button_warehouseFile = QPushButton("Choose warehouse file")
        warehouseFile = button_warehouseFile.clicked.connect(self.pickWarehouseFile)
        layout.addWidget(button_warehouseFile, 1, 1)

        label_warehouseFile = QLabel()
        label_warehouseFile.setText("Please choose a button_orderFile")
        layout.addWidget(label_warehouseFile, 1, 0)

        label_order = QLabel()
        label_order.setText("Pick order data")
        layout.addWidget(label_order, 2, 0)

        button_orderFile = QPushButton("Choose order file")
        orderFile = button_orderFile.clicked.connect(self.pickWarehouseFile)
        layout.addWidget(button_orderFile, 3, 1)

        label_orderFile = QLabel()
        label_orderFile.setText("Please choose a file")
        layout.addWidget(label_orderFile, 3, 0)

        self.buttongroup = QButtonGroup()
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)

        #create for every possible search algorithm a radiobutton and add it to
        #the created buttongroup
        for txt, val in self.algorithms:
            radiobutton = QRadioButton(txt)
            radiobutton.algorithm = val
            self.buttongroup.addButton(radiobutton, val)
            layout.addWidget(radiobutton, 3 + val, 0)

        button_execute = QPushButton("Execute search")
        button_execute.clicked.connect(self.execute)
        layout.addWidget(button_execute, 9, 0)

        button_quit = QPushButton("Quit")
        button_quit.clicked.connect(self.quit)
        layout.addWidget(button_quit, 9, 1)

    def execute(self):
        """
        Supposed to: pass on the value for algorithm_chosen, warehouse description
        and order
        At the time: only prints out Click and algorithm_chosen (integer)
        """
        print("Click" + str(self.algorithm_chosen))

    def quit(self):
        sys.exit()

    def on_button_clicked(self, id):
        """
        Input:
            self - object itself
            id - id of the clicked button
        checks which of the radiobutton is checked and stores it in a variable
        """
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                self.algorithm_chosen = button.algorithm
                print(self.algorithm_chosen)

    def pickWarehouseFile(self):
        return self.openFileNameDialog()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            return fileName

app = QApplication(sys.argv)
screen = App()
screen.show()
sys.exit(app.exec_())
