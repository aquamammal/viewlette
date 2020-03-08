from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QWidget):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 361)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Apptitle = QtWidgets.QLabel(self.centralwidget)
        self.Apptitle.setGeometry(QtCore.QRect(60, 20, 181, 41))

        font = QtGui.QFont()
        font.setPointSize(25)

        self.Apptitle.setFont(font)
        self.Apptitle.setAlignment(QtCore.Qt.AlignCenter)
        self.Apptitle.setObjectName("Apptitle")

        self.Addmoviebutton = QtWidgets.QPushButton(self.centralwidget)
        self.Addmoviebutton.setGeometry(QtCore.QRect(90, 150, 81, 20))
        self.Addmoviebutton.setObjectName("Addmoviebutton")

        self.Seenbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Seenbutton.setGeometry(QtCore.QRect(70, 270, 56, 17))
        self.Seenbutton.setObjectName("Seenbutton")

        self.Randommovielabel = QtWidgets.QLabel(self.centralwidget)
        self.Randommovielabel.setGeometry(QtCore.QRect(10, 210, 271, 41))

        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.Randommovielabel.setFont(font)
        self.Randommovielabel.setObjectName("Randommovielabel")

        self.Nextmoviebutton = QtWidgets.QPushButton(self.centralwidget)
        self.Nextmoviebutton.setGeometry(QtCore.QRect(150, 270, 56, 17))
        self.Nextmoviebutton.setObjectName("Nextmoviebutton")

        self.Movieaddedstatuslabel = QtWidgets.QLabel(self.centralwidget)
        self.Movieaddedstatuslabel.setGeometry(QtCore.QRect(30, 120, 221, 20))
        self.Movieaddedstatuslabel.setObjectName("Movieaddedstatuslabel")

        self.EnterMovieLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.EnterMovieLineEdit.setGeometry(QtCore.QRect(20, 70, 241, 20))
        self.EnterMovieLineEdit.setObjectName("EnterMovieLineEdit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Addmoviebutton.clicked.connect(self.btn_clk)
        self.Seenbutton.clicked.connect(self.btn_clk)
        self.Nextmoviebutton.clicked.connect(self.btn_clk)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Apptitle.setText(_translate("MainWindow", "VIEWLETTE"))
        self.Addmoviebutton.setText(_translate("MainWindow", "Add Movie to List"))
        self.Seenbutton.setText(_translate("MainWindow", "Seen"))
        self.Randommovielabel.setText(_translate("MainWindow", "Random Movie Is"))
        self.Nextmoviebutton.setText(_translate("MainWindow", "Next Movie"))
        self.Movieaddedstatuslabel.setText(_translate("MainWindow", "No Movie Added"))

    def btn_clk(self):
        sender = self.sender()

        if sender.text() == 'Add Movie to List':
            print(self.EnterMovieLineEdit.text())
        if sender.text() == 'Seen':
            print('seen button pressed')
        if sender.text() == 'Next Movie':
            print('Next Movie Button Pressed')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
