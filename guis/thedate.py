import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class DlgMain(QDialog):
    def __init__(self):
        print()
        super().__init__()
        self.setWindowTitle('My GUI')
        self.setGeometry(50, 50, 600, 600)
        s = QDate().currentDate()

        self.date = QDateTimeEdit(s, self)
        self.date.setCalendarPopup(True)
        self.date.move(50, 50)
        self.date.resize(100, 30)

        self.time = QDateTimeEdit(QTime.currentTime(), self)
        self.time.move(50, 100)

        self.date_time = QDateTimeEdit(QDateTime(s, QTime.currentTime()), self)
        self.date_time.move(50, 130)
        self.button = QPushButton('Elapsed time', self)
        self.button.move(200, 130)
        self.button.clicked.connect(self.clicked)

    def clicked(self):
        seconds = 0 - QDateTime.currentDateTime().secsTo(self.date_time.dateTime())
        print(seconds)
        set_time = self.date_time.dateTime().toString()
        QMessageBox.information(self, 'Elapsed time',
                                f'{seconds} have passed since {set_time}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DlgMain()
    main.show()
    sys.exit(app.exec())

