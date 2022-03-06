import sys
from PyQt6.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My GUI')
        self.setGeometry(50, 50, 500, 500)

        self.combo = QComboBox(self)
        self.combo.move(50, 50)
        # self.combo.addItems(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.combo.addItem('Apple', {'a': 'A', 'pop': 400402340})
        self.combo.addItem('Banana', {'b': 'B', 'pop': 400000000})
        self.fruitlabel = QLabel(f'Fruit: {self.combo.itemData(0)["pop"]}', self)
        self.combo.currentIndexChanged.connect(self.combo_changed)
        self.combo.highlighted.connect(self.combo_highlighted)

        self.edit_combo = QComboBox(self)
        self.edit_combo.move(200, 50)
        self.edit_combo.setEditable(True)
        self.edit_combo.setDuplicatesEnabled(False)
        self.edit_combo.addItem('Apple', 'a')
        self.edit_combo.addItem('Banana', 'b')
        self.edit_combo.currentIndexChanged.connect(self.edit_combo_changed)

    def edit_combo_changed(self, i):
        if not self.edit_combo.itemData(i):
            text, boo = QInputDialog.getText(self, 'Add Species Code',
            f'Add species code for {self.edit_combo.itemText(i)}')
            if boo:
                self.edit_combo.setItemData(i, text)
        QMessageBox.information(self, 'Plants', f'You selected {self.edit_combo.itemData(i)}')

    def combo_changed(self, i):
        self.fruitlabel.setText(f'Fruit: {self.combo.itemData(i)["pop"]}')
        QMessageBox.information(self, 'Combobox', f'You selected {self.combo.itemData(i)}')

    def combo_highlighted(self, i):
        self.fruitlabel.setText(f'HELLO  {self.combo.itemText(i)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DlgMain()
    main.show()
    sys.exit(app.exec())
