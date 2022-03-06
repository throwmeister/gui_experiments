import sys
from PyQt6.QtWidgets import *


class DlgMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My GUI')
        self.setGeometry(50, 50, 300, 300)
        # Widgets
        self.button0 = QPushButton('0')
        self.button1 = QPushButton('1')
        self.button2 = QPushButton('2')
        self.button3 = QPushButton('3')
        self.button4 = QPushButton('4')
        self.button5 = QPushButton('5')
        self.button6 = QPushButton('6')
        self.button7 = QPushButton('7')
        self.button8 = QPushButton('8')
        self.button9 = QPushButton('9')
        self.button_calc = QPushButton('Calculate')

        self.setup()

    def setup(self):
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.button1, 4, 0)
        self.main_layout.addWidget(self.button2, 4, 1)
        self.main_layout.addWidget(self.button3, 4, 2)
        self.main_layout.addWidget(self.button4, 3, 0)
        self.main_layout.addWidget(self.button5, 3, 1)
        self.main_layout.addWidget(self.button6, 3, 2)
        self.main_layout.addWidget(self.button7, 2, 0)
        self.main_layout.addWidget(self.button8, 2, 1)
        self.main_layout.addWidget(self.button9, 2, 2)
        self.main_layout.addWidget(self.button0, 5, 1)
        self.main_layout.addWidget(self.button_calc, 0, 0, 1, 3)
        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DlgMain()
    main.show()
    sys.exit(app.exec())

