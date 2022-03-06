import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My GUI')
        self.setGeometry(30, 30, 500, 500)

        self.button_update = QPushButton('Chose image', self)
        self.button_update.move(40, 40)
        self.button_update.clicked.connect(self.images)

    def images(self):
        img = QPixmap(100, 100)
        print(img)
        # More on this later

    def dates(self):
        dt = QDate.currentDate()
        print(dt.toString())
        print(dt.toJulianDay())
        print(dt.dayOfYear())
        print(dt.dayOfWeek())
        print(dt.addDays(23).toString())
        tn = QTime(14, 30, 15)
        print(tn.toString())
        tn2 = QTime(20, 15)
        print(tn2.toString())
        tn3 = tn.addSecs(138)
        print(tn3.toString())

    def fonts(self):
        font_1 = QFont('Times New Roman', 20, 75, True)
        self.button_update.setFont(font_1)
        font, boo = QFontDialog.getFont()
        print(font, boo)
        if boo:
            print(f'''{font.family()}
{font.italic()}
{font.bold()}
{font.weight()}
{font.pointSize()}
            ''')
            self.button_update.setFont(font)

    def colour(self):
        # RGB only
        c = QColorDialog.getColor(QColor(0, 225, 0), self, 'Chose colour')
        print(c)

    def file_handler(self):
        res = QFileDialog.getOpenFileNames(self, 'Open file', '', 'JPG File (*.jpg);; PNG File (*.png)')
        res2 = QFileDialog.getSaveFileName(self, 'Save file', 'Project 1', 'Python file (*.py)')

    def button_update_clicked(self):
        lips = ['red', 'blue', 'green']
        colour, boo = QInputDialog.getItem(self, 'Text', 'Enter your favourite colour: ', lips)
        # age, boo = QInputDialog.getInt(self, 'Text', 'Enter your age: ', 18, 18, 65, 1)
        # name, boo = QInputDialog.getText(self, 'text', 'Enter your name: ')
        if boo:
            QMessageBox.information(self, 'name', f'Your fav colour is {colour}')
        else:
            QMessageBox.critical(self, 'Canceled', 'You have not entered your colour')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec())

