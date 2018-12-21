import sys
from PyQt5.QtWidgets import *

class App(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Programming Task")

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("Test")
        layout.addWidget(label, 0, 0)



app = QApplication(sys.argv)
screen = App()
screen.show()
sys.exit(app.exec_())
