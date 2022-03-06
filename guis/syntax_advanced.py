import sys
from PyQt6.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My GUI')
        self.setGeometry(50, 50, 300, 300)

        # Tab Widget
        self.main = QHBoxLayout()
        self.tab = QTabWidget(self)
        self.tab.setTabPosition(QTabWidget.tabPosition(self.tab).East)
        self.tab.setMovable(True)
        self.tab.setTabsClosable(True)
        self.tab.tabCloseRequested.connect(self.empty)

        self.w1 = QWidget()
        self.w2 = QWidget()
        self.w3 = QWidget()
        self.w4 = QWidget()
        self.w5 = QWidget()
        self.tab.addTab(self.w1, '1')
        self.tab.addTab(self.w2, '2')
        self.tab.addTab(self.w3, '3')
        self.tab.addTab(self.w4, '4')
        self.tab.setTabText(2, 'changed')
        self.tab.insertTab(2, self.w5, '5')
        self.main.addWidget(self.tab)

        # QList Widgets

    def empty(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DlgMain()
    main.show()
    sys.exit(app.exec())

