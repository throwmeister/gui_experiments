import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My GUI')

        # Widgets
        self.button = QPushButton('Button 2')
        self.line_edit = QLineEdit('Edit this line')
        self.line_edit2 = QLineEdit('Edit this line too')
        self.d = QDateTimeEdit(self)
        self.spin = QSpinBox(self)
        self.main_layout = QFormLayout()
        self.main_layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        self.main_layout.setRowWrapPolicy(QFormLayout.rowWrapPolicy(self.main_layout).WrapLongRows)
        self.main_layout.addRow('First name: ', self.line_edit)
        self.main_layout.addRow('Last name: ', self.line_edit2)
        self.main_layout.addRow('Age: ', self.d)
        self.main_layout.addRow('Date started: ', self.spin)
        self.main_layout.addRow('Date started: ', self.spin)
        self.main_layout.addRow('Submit: ', self.button)

        self.setLayout(self.main_layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DlgMain()
    main.show()
    sys.exit(app.exec())

