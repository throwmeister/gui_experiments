import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.check_three = None
        self.setWindowTitle('My GUI')
        self.setGeometry(50, 50, 500, 500)
        self.button_update = QCheckBox('hello', self)
        self.label = QLabel('Old text', self)
        self.label.resize(300, 300)
        self.label.move(40, 100)
        font = QFont('Times New Roman', 20, 75, True)
        self.label.setFont(font)

    def check_box_main(self):
        self.button_update = QCheckBox('Enabled', self)
        self.button_update.move(30, 40)
        self.button_update.setChecked(True)
        self.check_three = QCheckBox('Three state', self)
        self.check_three.setTristate(True)
        self.check_three.move(30, 70)
        self.check_three.stateChanged.connect(self.check_box_three)
        self.button_update.toggled.connect(self.check_box)

    def check_box_three(self, boo):
        print(boo)
        if boo == 0:
            QMessageBox.information(self, 'State', 'Unchecked')
        elif boo == 1:
            QMessageBox.information(self, 'State', 'Partially checked')
        else:
            QMessageBox.information(self, 'State', 'Checked')

    def check_box(self, boo):
        if boo:
            self.label.setDisabled(False)
        else:
            self.label.setDisabled(True)

    def push_button_main(self):
        self.button_update = QPushButton('Change label', self)
        self.button_update.move(40, 40)
        self.button_update.setIcon(QIcon(QPixmap('C:/Users/alexa/Downloads/sunset.jpg')))
        self.button_update.resize(140, 100)
        self.button_update.setFlat(True)

        self.button_update.clicked.connect(self.push_button)

    def push_button(self):
        if self.label.isEnabled():
            self.label.setDisabled(True)
            self.label.setText('Enable label')
        else:
            self.label.setEnabled(True)
            self.label.setText('Disable label')

    def image_labels(self):
        self.label.setText('New text')
        file, tp = QFileDialog.getOpenFileName(self, 'Open file', '', 'JPG File (*.jpg);; PNG File (*.png)')
        print(file)
        pxm = QPixmap(file).scaled(300, 300)
        self.label.setPixmap(pxm)
        self.label.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DlgMain()
    window.show()
    sys.exit(app.exec())
