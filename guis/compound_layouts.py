import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My GUI')
        self.setGeometry(50, 50, 300, 300)

        self.combo = QComboBox()
        self.combo.addItems(['General', 'Species', 'Location', 'Surveys'])
        self.general = QWidget(self)
        self.species = QWidget()
        self.location = QWidget()
        self.w_surveys = QWidget()

        self.nest = QLabel('34')
        self.date_found = QDateTimeEdit(QDate(2016, 13, 5))
        self.date_last = QDateTimeEdit(QDate(2020, 13, 5))
        self.active = QCheckBox()

        self.combo_species = QComboBox()
        self.combo_species.addItem('Huh', 800)
        self.combo_species.addItem('Hawk', 400)
        self.combo_species.addItem('Other', 1600)

        self.edit_species = QLineEdit()
        self.buffer = QSpinBox()
        self.buffer.setValue(800)

        self.lat = QDoubleSpinBox()
        self.long = QDoubleSpinBox()

        self.surveys = QListWidget()
        self.surveys.addItem('1')
        self.surveys.addItem('2')
        self.surveys.addItem('3')
        self.surveys.addItem('4')
        self.add_survey = QPushButton('Add survey')

        self.setup()

    def setup(self):
        self.main = QHBoxLayout()
        self.left = QVBoxLayout()
        self.right = QStackedLayout()

        self.main.addLayout(self.left)
        self.main.addLayout(self.right)

        self.left.addWidget(self.general)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DlgMain()
    main.show()
    sys.exit(app.exec())

