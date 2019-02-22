import sys
from PyQt5.QtWidgets import * #this will be the GUI package on which the GUI for the project is built
from functionality import preprocess_info

oPSUs = {}


class App(QWidget): # creates the containing interface with possible options for the app user
    # names the variable ("algorithm") that indicates type of search used later in code in succeeding methods
    algorithms = [
    ("Hill Climbing", 1),
    ("First Choice Hill Climbing", 2),
    ("Random Restart Hill Climbing", 3),
    ("Simulated Annealing", 4),
    ("Local Beam Search", 5)] #defines strings which will appear as options for user
    algorithm_chosen = 0 #initializes app without a search type being chosen
    warehouseFile = ""
    orderFile = ""
    def __init__(self): # sets up GUI window and layout; this particular instance known as "self"
        QWidget.__init__(self)
        self.setWindowTitle("Programming Task")

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        #create elements (Widgets) and specifying label and location

        self.label_warehouse = QLabel()
        self.label_warehouse.setText("Pick data to set up warehouse")
        self.layout.addWidget(self.label_warehouse, 0, 0)

        self.button_warehouseFile = QPushButton("Choose warehouse file")
        self.button_warehouseFile.clicked.connect(self.pickWarehouseFile)
        self.layout.addWidget(self.button_warehouseFile, 1, 1)

        self.label_warehouseFile = QLabel()
        self.label_warehouseFile.setText(self.warehouseFile)
        self.layout.addWidget(self.label_warehouseFile, 1, 0)

        self.label_order = QLabel()
        self.label_order.setText("Pick order data")
        self.layout.addWidget(self.label_order, 2, 0)

        self.button_orderFile = QPushButton("Choose order file")
        self.button_orderFile.clicked.connect(self.pickOrderFile)
        self.layout.addWidget(self.button_orderFile, 3, 1)

        self.label_orderFile = QLabel()
        self.label_orderFile.setText("Please choose a file")
        self.layout.addWidget(self.label_orderFile, 3, 0)

        #create buttongroup to group radio buttons together to ensure all options/unintended options aren't chosen
        self.buttongroup = QButtonGroup()
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)

        #create for every possible search algorithm a radiobutton and add it to
        #the previously created button group (line 46)
        for txt, val in self.algorithms:
            self.radiobutton = QRadioButton(txt)
            self.radiobutton.algorithm = val
            self.buttongroup.addButton(self.radiobutton, val)
            self.layout.addWidget(self.radiobutton, 3 + val, 0)



        self.button_execute = QPushButton("Execute search")
        self.button_execute.clicked.connect(self.execute)
        self.layout.addWidget(self.button_execute, 9, 0)

        self.button_quit = QPushButton("Quit")
        self.button_quit.clicked.connect(self.quit)
        self.layout.addWidget(self.button_quit, 9, 1)

    def execute(self):
        """
        Method:
            pass on the value for algorithm_chosen, warehouse description
            and order, values for search functions as needed (e.g., temperature for
            Simmulated Annealing)
        """
        global oPSUs
        oPSUs = {}
        if self.algorithm_chosen > 2:
            user_input = self.getValue()
            oPSUs = preprocess_info(self.warehouseFile, self.orderFile, self.algorithm_chosen, user_input)
        else:
            oPSUs = preprocess_info(self.warehouseFile, self.orderFile, self.algorithm_chosen, 0)
        self.showResults()

    def showResults(self):
        self.resultDialog = ShowResults()
        self.resultDialog.show()

    def getValue(self):
        """
        Method:
            opens up Input Dialog that requests additional information if Simulated Annealing,
            Prallel Hill Climbing or Local Beam Search is chosen and stores info in variable
        """
        i, okPressed = QInputDialog.getInt(self, "Get integer","Provide necessary value:", 28, 0, 100, 1)
        if okPressed:
            return i

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
        Method:
            checks which of the radiobutton is checked and stores it in a variable
        """
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                self.algorithm_chosen = button.algorithm
                print(self.algorithm_chosen)

    def pickWarehouseFile(self):
        """
        calls on file picker method to choose warehouse file and store path in
        a variable
        """
        ware = self.openFileNameDialog()
        self.label_warehouseFile.setText(ware)
        self.warehouseFile = ware
        return ware

    def pickOrderFile(self):
        """
        calls on file picker method to choose order file and store path in
        a variable
        """
        order = self.openFileNameDialog()
        self.label_orderFile.setText(order)
        self.orderFile = order
        return order

    def openFileNameDialog(self):
        """
        opens up a file picker dialog
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Choose Files", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            return fileName


class ShowResults(QScrollArea):
    def __init__(self):
        global oPSUs

        super().__init__()
        self.setWindowTitle("Result")

        self.widget = QWidget()
        self.layout2 = QVBoxLayout(self.widget)

        self.numberPSUS = QLabel()
        self.numberPSUS.setText("eligible PSUs:" + str(len(oPSUs)))
        self.layout2.addWidget(self.numberPSUS)

        for x in oPSUs:
            self.labelPSU = QLabel()
            str1 = ', '.join(oPSUs[x])
            self.labelPSU.setText(str(x) + ": " + str1)
            self.layout2.addWidget(self.labelPSU)

        self.button_ok = QPushButton("Ok")
        self.button_ok.clicked.connect(self.close)
        self.layout2.addWidget(self.button_ok)

        self.setWidget(self.widget)
        self.setWidgetResizable(True)


app = QApplication(sys.argv)
screen = App()
screen.show()
sys.exit(app.exec_())
