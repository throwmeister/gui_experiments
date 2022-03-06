import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My GUI')
        self.setGeometry(50, 50, 300, 300)

        self.label = QLabel('My label', self)
        self.label.move(100, 20)
        self.radio_r = QRadioButton('Red', self)
        self.radio_b = QRadioButton('Blue', self)
        self.radio_g = QRadioButton('Green', self)
        self.radio_g.move(30, 100)
        self.radio_r.move(30, 40)
        self.radio_b.move(30, 70)
        self.radio_r.setChecked(True)
        self.radio_r.clicked.connect(self.radio_clicked)
        self.radio_g.clicked.connect(self.radio_clicked)
        self.radio_b.clicked.connect(self.radio_clicked)
        self.radio_small = QRadioButton('Small Text', self).move(30, 130)
        self.radio_medium = QRadioButton('Medium Text', self).move(30, 160)
        self.radio_large = QRadioButton('Large Text', self).move(30, 190)

    def radio_clicked(self):
        rbt = self.sender()
        style = f'Colour {rbt.text()}'
        print(style)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DlgMain()
    main.show()
    sys.exit(app.exec())
