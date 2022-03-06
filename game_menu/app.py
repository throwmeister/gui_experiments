import sys
import ctypes
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QPixmap, QBrush, QLinearGradient
from PyQt6.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()

        style = '''
        QDialog{
        background-image: url(main_menu_background.jpg);
               }
               


            QPushButton{
                background-color: #ebc17a;
                border-radius: 5px;
                border: 6px groove #d9a143
            }
            QPushButton:hover{
            background-color: #e3c086;
            outline: none

            }
        '''
        # background-color: #66e35b;
        # border-radius: 5px;
        # border: 6px groove #156b15
        self.setStyleSheet(style)

        self.setWindowTitle('My GUI')
        user32 = ctypes.windll.user32
        self.resize(user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
        self.setWindowTitle('Wickman\'s game 😂')
        self.init_ui()

    def init_ui(self):
        self.main_label = QLabel('🅿🅾🅺🅴🆁 🅰🅽🅳 🅱🅻🅰🅲🅺🅹🅰🅲🅺')
        self.main_label.setStyleSheet('font-size: 45px; color: black')
        self.play = QPushButton('Play')
        self.play.clicked.connect(self.chose_options)
        self.settings = QPushButton('Settings')
        self.exit = QPushButton('Exit game')
        self.exit.clicked.connect(lambda _: self.close())

        main_layout = QVBoxLayout()
        bottom_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addStretch()
        main_layout.addLayout(bottom_layout)
        main_layout.addStretch()
        # self.main_label.setStyleSheet()
        self.main_label.setAlignment(QLabel.alignment(self.main_label).AlignHCenter)
        top_layout.addWidget(self.main_label)

        self.play.setFixedSize(450, 100)
        self.exit.setFixedSize(450, 100)
        self.settings.setFixedSize(450, 100)
        centered = Qt.AlignmentFlag.AlignCenter


        bottom_layout.addWidget(self.play, alignment=centered)
        bottom_layout.addWidget(self.settings, alignment=centered)
        bottom_layout.addWidget(self.exit, alignment=centered)
        self.setLayout(main_layout)
        self.repaint()

    def chose_options(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DlgMain()
    main.showMaximized()
    main.show()
    sys.exit(app.exec())
