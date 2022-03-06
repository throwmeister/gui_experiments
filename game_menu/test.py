import sys
import ctypes
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QPixmap, QBrush
from PyQt6.QtCore import *


class DlgMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My GUI')
        user32 = ctypes.windll.user32
        self.resize(user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
        self.show_ui()

    def show_ui(self):
        button = QPushButton('ehllo', self)
        button2 = QPushButton('hi', self)
        layout = QHBoxLayout()
        layout.addWidget(button)
        layout.addWidget(button2)
        stack = QStackedWidget()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QMainWindow{
        background-image: url(main_menu_background.jpg)}
        ''')
    main = DlgMain()
    main.showMaximized()
    sys.exit(app.exec())

"""QWidget{
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 175, 255, 255), stop:0.512438 rgba(194, 61, 235, 255), stop:0.98 rgba(66, 176, 255, 255), stop:1 rgba(0, 0, 0, 0));

}

QLabel{

}

QPushButton{
				
	color: rgb(0, 85, 0);
                
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(102, 163, 255, 255), stop:0.55 rgba(181, 61, 235, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));
                border-radius: 5px;
                border: 6px groove rgb(0, 0, 0)
            }
            QPushButton:hover{
            background-color: transparent;
            outline: none

            }"""