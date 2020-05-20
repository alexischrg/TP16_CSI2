from PySide2.QtWidgets import *

class IHM(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("IHM")
        self.setMinimumSize(100,100)
        self.layout = QHBoxLayout()

        self.bar = QProgressBar()
        self.slider = QSlider()

        self.layout.addWidget(self.bar)
        self.layout.addWidget(self.slider)

        self.slider.valueChanged.connect(self.ProgressBar)

        self.setLayout(self.layout)

    def ProgressBar(self):
        self.bar.setValue(self.slider.value())



if __name__ == "__main__":
   app = QApplication([])
   win = IHM()
   win.show()
   app.exec_()