import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTimer


class DlgMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Time')
        self.setGeometry(50, 50, 350, 350)
        self.label = QLabel(self)
        self.label.resize(250, 250)
        self.label.setStyleSheet('background-color:green')
        self.label.move(40, 20)
        self.start = QPushButton('start', self)
        self.start.move(100, 300)
        self.stop = QPushButton('stop', self)
        self.stop.move(190, 300)

        self.start.clicked.connect(self.s)
        self.stop.clicked.connect(self.sp)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.change_colour)
        self.value = 0

    def s(self):
        self.timer.start()

    def sp(self):
        self.timer.stop()

    def change_colour(self):
        if self.value == 0:
            self.label.setStyleSheet('background-color:yellow')
            self.value = 1
        else:
            self.label.setStyleSheet('background-color:red')
            self.value = 0



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DlgMain()
    main.show()
    sys.exit(app.exec())
