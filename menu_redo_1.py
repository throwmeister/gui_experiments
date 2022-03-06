from PyQt5 import QtCore, QtGui, QtWidgets


class Menu(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1054, 860)
        Form.setStyleSheet("QWidget{\n"
                           "    background-color: rgb(15, 102, 72);\n"
                           "    \n"
                           "}\n"
                           "\n"
                           "QLabel{\n"
                           "\n"
                           "}\n"
                           "\n"
                           "QPushButton{\n"
                           "    font-family: MS Shell Dlg 2;\n"
                           "    font-size: 30px;\n"
                           "                \n"
                           "    color: rgb(0, 85, 0);\n"
                           "                \n"
                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 132, 93, 255), stop:1 rgba(97, 192, 164, 255));\n"
                           "                border-radius: 3px;\n"
                           "                border: 2px groove rgb(0, 0, 0)\n"
                           "            }\n"
                           "            QPushButton:hover{\n"
                           "            background-color: #e3c086;\n"
                           "            outline: none\n"
                           "            }")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.main_stack = QtWidgets.QStackedWidget(Form)
        self.main_stack.setObjectName("main_stack")
        self.main_menu = QtWidgets.QWidget()
        self.main_menu.setObjectName("main_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.play_button = QtWidgets.QPushButton(self.main_menu)
        self.play_button.setMinimumSize(QtCore.QSize(450, 100))
        self.play_button.setMaximumSize(QtCore.QSize(450, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.play_button.setFont(font)
        self.play_button.setObjectName("play_button")
        self.verticalLayout_2.addWidget(self.play_button, 0, QtCore.Qt.AlignHCenter)
        self.settings_button = QtWidgets.QPushButton(self.main_menu)
        self.settings_button.setMinimumSize(QtCore.QSize(450, 100))
        self.settings_button.setMaximumSize(QtCore.QSize(450, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.settings_button.setFont(font)
        self.settings_button.setObjectName("settings_button")
        self.verticalLayout_2.addWidget(self.settings_button, 0, QtCore.Qt.AlignHCenter)
        self.exit_button = QtWidgets.QPushButton(self.main_menu)
        self.exit_button.setMinimumSize(QtCore.QSize(450, 100))
        self.exit_button.setMaximumSize(QtCore.QSize(450, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout_2.addWidget(self.exit_button, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.main_stack.addWidget(self.main_menu)
        self.p_or_b = QtWidgets.QWidget()
        self.p_or_b.setObjectName("p_or_b")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.p_or_b)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.backbutton = QtWidgets.QPushButton(self.p_or_b)
        self.backbutton.setEnabled(True)
        self.backbutton.setMinimumSize(QtCore.QSize(100, 40))
        self.backbutton.setMaximumSize(QtCore.QSize(100, 40))
        self.backbutton.setStyleSheet("border-style: outset;")
        self.backbutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/alexa/Documents/POKER_BLACKJACK_UIS\\back button.png"),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.backbutton.setIcon(icon)
        self.backbutton.setObjectName("backbutton")
        self.gridLayout_3.addWidget(self.backbutton, 0, 1, 1, 1, QtCore.Qt.AlignBottom)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 3, 1, 1)
        self.bj_lobby_button = QtWidgets.QPushButton(self.p_or_b)
        self.bj_lobby_button.setMinimumSize(QtCore.QSize(450, 450))
        self.bj_lobby_button.setMaximumSize(QtCore.QSize(650, 450))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.bj_lobby_button.setFont(font)
        self.bj_lobby_button.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.bj_lobby_button, 1, 2, 1, 1, QtCore.Qt.AlignVCenter)
        self.pk_lobby_button = QtWidgets.QPushButton(self.p_or_b)
        self.pk_lobby_button.setMinimumSize(QtCore.QSize(450, 450))
        self.pk_lobby_button.setMaximumSize(QtCore.QSize(650, 450))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(-1)
        self.pk_lobby_button.setFont(font)
        self.pk_lobby_button.setStyleSheet("")
        self.pk_lobby_button.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pk_lobby_button, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem6, 0, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        self.main_stack.addWidget(self.p_or_b)
        self.lobby = QtWidgets.QWidget()
        self.lobby.setObjectName("lobby")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.lobby)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lobby_table = QtWidgets.QListWidget(self.lobby)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lobby_table.setFont(font)
        self.lobby_table.setStyleSheet("             background-color: #ebc17a;\n"
                                       "                border: 6px groove #d9a143")
        self.lobby_table.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.lobby_table.addItem(item)
        self.verticalLayout_5.addWidget(self.lobby_table)
        self.add_player_button = QtWidgets.QPushButton(self.lobby)
        self.add_player_button.setMinimumSize(QtCore.QSize(0, 50))
        self.add_player_button.setObjectName("pushButton_5")
        self.verticalLayout_5.addWidget(self.add_player_button)
        self.remove_player_button = QtWidgets.QPushButton(self.lobby)
        self.remove_player_button.setMinimumSize(QtCore.QSize(0, 50))
        self.remove_player_button.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.remove_player_button)
        self.ready_game_button = QtWidgets.QPushButton(self.lobby)
        self.ready_game_button.setMinimumSize(QtCore.QSize(0, 50))
        self.ready_game_button.setObjectName("pushButton_6")
        self.verticalLayout_5.addWidget(self.ready_game_button)
        self.exit_lobby_button = QtWidgets.QPushButton(self.lobby)
        self.exit_lobby_button.setMinimumSize(QtCore.QSize(0, 50))
        self.exit_lobby_button.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.exit_lobby_button)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.main_stack.addWidget(self.lobby)
        self.gridLayout.addWidget(self.main_stack, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.main_stack.setCurrentIndex(0)
        self.exit_button.clicked.connect(Form.close)  # type: ignore
        self.play_button.clicked.connect(lambda _: self.main_stack.setCurrentIndex(1))
        self.backbutton.clicked.connect(lambda _: self.main_stack.setCurrentIndex(0))
        self.pk_lobby_button.clicked.connect(self.setup_poker_lobby)
        self.bj_lobby_button.clicked.connect(self.setup_blackjack_lobby)
        self.exit_lobby_button.clicked.connect(self.reset_lobby)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.play_button.setText(_translate("Form", "Play"))
        self.settings_button.setText(_translate("Form", "Settings"))
        self.exit_button.setText(_translate("Form", "Exit"))
        self.bj_lobby_button.setText(_translate("Form", "Blackjack"))
        self.pk_lobby_button.setText(_translate("Form", "Poker"))
        __sortingEnabled = self.lobby_table.isSortingEnabled()
        self.lobby_table.setSortingEnabled(False)
        item = self.lobby_table.item(0)
        item.setText(_translate("Form", "Player 1"))
        self.lobby_table.setSortingEnabled(__sortingEnabled)
        self.add_player_button.setText(_translate("Form", "Join lobby"))
        self.remove_player_button.setText(_translate("Form", "Leave lobby"))
        self.ready_game_button.setText(_translate("Form", "Ready lobby"))
        self.exit_lobby_button.setText(_translate("Form", "Exit lobby"))
        self.title.setText(_translate("Form", "🅿🅾🅺🅴🆁 🅰🅽🅳 🅱🅻🅰🅲🅺🅹🅰🅲🅺"))

    def setup_poker_lobby(self):
        self.main_stack.setCurrentIndex(2)
        # Pass information that will help setup the poker game

    def setup_blackjack_lobby(self):
        self.main_stack.setCurrentIndex(2)
        # Pass imformation that will help setup the blackjack game

    def reset_lobby(self):
        self.lobby_table.clear()
        self.main_stack.setCurrentIndex(1)





if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QWidget()
    ui = Menu()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())


