from PySide2.QtWidgets import *
from random import *

class CycleIsen(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setFixedSize(500,300)
        self.setWindowTitle("Cycles de l'ISEN Yncréa Ouest")

        self.layout = QVBoxLayout()

        self.label = QLabel("CSI")
        self.button = QPushButton("Changer le cycle")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.buttonclicked)

        self.setLayout(self.layout)


    def buttonclicked(self):
        lst = ["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]
        res = randint(0, 5)
        self.label.setText(lst[res])

if __name__ == "__main__":
   app = QApplication([])
   win = CycleIsen()
   win.show()
   app.exec_()