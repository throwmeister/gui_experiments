import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer

count = 0
class DlgMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My GUI')
        self.setGeometry(50, 50, 300, 300)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        self.timer = QTimer()
        self.progress_bar = QProgressBar()
        self.start_b = QPushButton('Start')
        self.stop_b = QPushButton('Stop')

        self.timer.setInterval(100)
        self.timer.timeout.connect(self.run_progress)
        self.start_b.clicked.connect(self.start)
        self.stop_b.clicked.connect(self.stop)

        vbox.addWidget(self.progress_bar)
        vbox.addLayout(hbox)

        hbox.addWidget(self.start_b)
        hbox.addWidget(self.stop_b)

        self.setLayout(vbox)

    def run_progress(self):
        global count
        count += 1
        print(count)
        self.progress_bar.setValue(count)

    def start(self):
        self.timer.start()

    def stop(self):
        global count
        self.timer.stop()
        count = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DlgMain()
    main.show()
    sys.exit(app.exec())

