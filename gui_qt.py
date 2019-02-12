import sys
from PyQt5.QtWidgets import * #this will be the GUI package on which the GUI for the project is built

class App(QWidget): # creates the containing interface with possible options for the app user
    algorithms = [ #names the variable ("algorithm") that indicates type of search used later in code in suceeding methods
    ("Hill Climbing", 1),
    ("First Choice Hill Climbing", 2),
    ("Parallel Hill Climbing", 3),
    ("Simulated Annealing", 4),
    ("Local Beam Search", 5)] #defines strings which will appear as options for user
    algorithm_chosen = 0 #initializes app without a search type being chosen
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

        #input number of parallel hill Climbing searches to run
        self.input_parallel = QLineEdit()
        self.input_parallel.setPlaceholderText("Number of Parallel Searches to Run")
        self.layout.addWidget(self.input_parallel, 6, 1)

        #for Simulated Annealing option, allows user input for temperatures in process
        self.input_temp = QLineEdit()
        self.input_temp.setPlaceholderText("Value for Temperature")
        self.layout.addWidget(self.input_temp, 7, 1)

        #for Local Beam Search, allows user input to specify number of steps in process
        self.input_beam = QLineEdit()
        self.input_beam.setPlaceholderText("Steps for Beam Search")
        self.layout.addWidget(self.input_beam, 8, 1)

        self.button_execute = QPushButton("Execute search")
        self.button_execute.clicked.connect(self.execute)
        self.layout.addWidget(self.button_execute, 9, 0)

        self.button_quit = QPushButton("Quit")
        self.button_quit.clicked.connect(self.quit)
        self.layout.addWidget(self.button_quit, 9, 1)

    def execute(self):
        """
        Supposed to: pass on the value for algorithm_chosen, warehouse description
        and order, values for search functions as needed (e.g., temperature for
        Simmulated Annealing)
        At the time: only prints out "Click" and algorithm_chosen (integer)

        To do:

        GUI
        redo value input for search algorithms -> validity method
        execute method -> which algorithm is choosen
        new method: check for validity of input

        GUI passes on information to execute ->
        Functionality
        read in text files ; how to represent text file:
        PSU: dictionary: key = psu; value = item in psu
        Warehouse: list = items
        First Check: warehouse content to see if warehouse has wanted items
        Do Search
        Print number of psu's used and which psu with which items exactly

        ? How do we represent neighborhood and how do we ensure that the search just looks where the needed items are s
        ? Preprocessing: allow only psu's in the neighborhood that have at least one item of the items we want

        Step 1: order files
        Step 2: warehouse file
        Step 3: check if items of order list are in warehouse
        Step 4: go through psu's and pull out the ones that have a item that is wanted (Preprocessing), create dictionary that has the psu with the items
        Step 5: search algorithm finds the best combination of visited psu's
        Step 6: #fml

        ? How to do constraints ? How to order? How to have a good objective function? 

        """
        if(self.algorithm_chosen == 3):
            parallelsteps = self.input_parallel.text()
            if parallesteps <= 0:
                print("Please input a valid value")
        else if(self.algorithm_chosen == 4):
            temperature = self.input_temp.text()
        else if(self.algorithm_chosen == 5):
             beamsteps = self.input_beam.text()
         else:






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
