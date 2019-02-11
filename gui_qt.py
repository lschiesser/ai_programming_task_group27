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

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        #create buttongroup to group radiobuttons together
        self.label_warehouse = QLabel()
        self.label_warehouse.setText("Pick data to set up warehouse")
        self.layout.addWidget(self.label_warehouse, 0, 0)

        self.button_warehouseFile = QPushButton("Choose warehouse file")
        self.warehouseFile = self.button_warehouseFile.clicked.connect(self.pickWarehouseFile)
        self.layout.addWidget(self.button_warehouseFile, 1, 1)

        self.label_warehouseFile = QLabel()
        self.label_warehouseFile.setText(self.warehouseFile)
        self.layout.addWidget(self.label_warehouseFile, 1, 0)

        self.label_order = QLabel()
        self.label_order.setText("Pick order data")
        self.layout.addWidget(self.label_order, 2, 0)

        self.button_orderFile = QPushButton("Choose order file")
        self.orderFile = self.button_orderFile.clicked.connect(self.pickWarehouseFile)
        self.layout.addWidget(self.button_orderFile, 3, 1)

        self.label_orderFile = QLabel()
        self.label_orderFile.setText("Please choose a file")
        self.layout.addWidget(self.label_orderFile, 3, 0)

        self.buttongroup = QButtonGroup()
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)

        #create for every possible search algorithm a radiobutton and add it to
        #the created buttongroup
        for txt, val in self.algorithms:
            self.radiobutton = QRadioButton(txt)
            self.radiobutton.algorithm = val
            self.buttongroup.addButton(self.radiobutton, val)
            self.layout.addWidget(self.radiobutton, 3 + val, 0)

        self.input_temp = QLineEdit()
        self.input_temp.setPlaceholderText("Value for Temperature")
        self.layout.addWidget(self.input_temp, 7, 1)

        self.button_execute = QPushButton("Execute search")
        self.button_execute.clicked.connect(self.execute)
        self.layout.addWidget(self.button_execute, 9, 0)

        self.button_quit = QPushButton("Quit")
        self.button_quit.clicked.connect(self.quit)
        self.layout.addWidget(self.button_quit, 9, 1)

    def execute(self):
        """
        Supposed to: pass on the value for algorithm_chosen, warehouse description
        and order
        At the time: only prints out Click and algorithm_chosen (integer)
        """
        temperature = self.input_temp.text()
        if(temperature):
            print(temperature)
        print("Click" + str(self.algorithm_chosen))

    def quit(self):
        """
        Quits the program
        """
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
