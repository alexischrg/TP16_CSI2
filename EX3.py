from PySide2.QtWidgets import *

class IHM(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("IHM")
        self.setMinimumSize(200,200)
        self.layout = QVBoxLayout()
        self.nb = 0

        self.button = QPushButton("Changer mon texte !")
        self.text = QTextEdit("le nombre de clics va être affiché ici")

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text)

        self.button.clicked.connect(self.buttonChange)

        self.setLayout(self.layout)

    def buttonChange(self):
        self.nb += 1
        self.button.setText("clic "+str(self.nb))
        self.text.setText("clic "+str(self.nb))
        print("clic",self.nb)
        return



if __name__ == "__main__":
   app = QApplication([])
   win = IHM()
   win.show()
   app.exec_()