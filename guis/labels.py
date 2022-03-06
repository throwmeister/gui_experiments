import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    #  First lecture
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Labels')
        self.setGeometry(50, 50, 350, 350)
        self.button()

    # Second lecture - labels
    def ui(self):
        text1 = QLabel('Hello python', self)
        text2 = QLabel('Hello world', self)
        text1.move(100, 50)
        text2.move(200, 100) # x, y
        self.show()

    # Third lecture - buttons
    def button(self):
        text = QLabel('My text', self)
        enter_button = QPushButton('Enter', self)
        exit_button = QPushButton('Exit', self)
        text.move(160, 50)
        enter_button.move(200, 80)
        exit_button.move(100, 80)
        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
