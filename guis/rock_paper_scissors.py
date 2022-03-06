import sys
from PyQt6.QtWidgets import *


class DlgMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My GUI')
        self.setGeometry(50, 50, 300, 300)

        hbx = QHBoxLayout()
        button1 = QPushButton('Play')
        hbx.addStretch()
        hbx.addWidget(button1)
        hbx.setStretch(0, 0)
        hbx.addStretch()
        self.setLayout(hbx)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DlgMain()
    main.show()
    sys.exit(app.exec())

