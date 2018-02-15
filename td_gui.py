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
        TapeDriveWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        TapeDriveWindow.setStyleSheet("TapeDriveWindow {qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.centralwidget = QtWidgets.QWidget(TapeDriveWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.consoleOut = QtWidgets.QTextBrowser(self.centralwidget)
        self.consoleOut.setGeometry(QtCore.QRect(10, 30, 256, 192))
        self.consoleOut.setObjectName("consoleOut")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 60, 16))
        self.label.setObjectName("label")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(540, 260, 21, 160))
        self.verticalSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalSlider.setMinimum(1)
        self.verticalSlider.setMaximum(359)
        self.verticalSlider.setSingleStep(1)
        self.verticalSlider.setPageStep(45)
        self.verticalSlider.setSliderPosition(45)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider.setTickInterval(15)
        self.verticalSlider.setObjectName("verticalSlider")
        self.btnHome_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnHome_2.setGeometry(QtCore.QRect(380, 30, 91, 81))
        self.btnHome_2.setObjectName("btnHome_2")
        self.btnBackward = QtWidgets.QPushButton(self.centralwidget)
        self.btnBackward.setGeometry(QtCore.QRect(280, 30, 91, 81))
        self.btnBackward.setObjectName("btnBackward")
        self.btnForward = QtWidgets.QPushButton(self.centralwidget)
        self.btnForward.setGeometry(QtCore.QRect(280, 110, 91, 81))
        self.btnForward.setObjectName("btnForward")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 240, 101, 20))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(570, 260, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setReadOnly(True)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(359)
        self.spinBox.setProperty("value", 45)
        self.spinBox.setObjectName("spinBox")
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
        self.label.setText(_translate("TapeDriveWindow", "Log"))
        self.verticalSlider.setToolTip(_translate("TapeDriveWindow", "<html><head/><body><p>Drag to change step size. Step will be when slider is released.</p></body></html>"))
        self.btnHome_2.setText(_translate("TapeDriveWindow", "Home"))
        self.btnBackward.setText(_translate("TapeDriveWindow", "Backward"))
        self.btnForward.setText(_translate("TapeDriveWindow", "Forward"))
        self.label_2.setText(_translate("TapeDriveWindow", "Step Size (deg)"))

