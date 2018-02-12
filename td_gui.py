# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'td_gui.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TapeDriveWindow(object):
    def setupUi(self, TapeDriveWindow):
        TapeDriveWindow.setObjectName("TapeDriveWindow")
        TapeDriveWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(TapeDriveWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 10, 101, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 90, 101, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 256, 192))
        self.listWidget.setObjectName("listWidget")
        TapeDriveWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TapeDriveWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        TapeDriveWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TapeDriveWindow)
        self.statusbar.setObjectName("statusbar")
        TapeDriveWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TapeDriveWindow)
        QtCore.QMetaObject.connectSlotsByName(TapeDriveWindow)

    def retranslateUi(self, TapeDriveWindow):
        _translate = QtCore.QCoreApplication.translate
        TapeDriveWindow.setWindowTitle(_translate("TapeDriveWindow", "Tape Drive Control"))
        self.pushButton.setText(_translate("TapeDriveWindow", "Connect"))
        self.pushButton_2.setText(_translate("TapeDriveWindow", "Disconnect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TapeDriveWindow = QtWidgets.QMainWindow()
    ui = Ui_TapeDriveWindow()
    ui.setupUi(TapeDriveWindow)
    TapeDriveWindow.show()
    sys.exit(app.exec_())

