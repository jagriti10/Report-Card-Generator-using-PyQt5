# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'faltu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_resultwindow(object):
    def setupUi(self, resultwindow):
        resultwindow.setObjectName("resultwindow")
        resultwindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(resultwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(200, 270, 96, 23))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(200, 340, 96, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        resultwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(resultwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        resultwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(resultwindow)
        self.statusbar.setObjectName("statusbar")
        resultwindow.setStatusBar(self.statusbar)

        self.retranslateUi(resultwindow)
        QtCore.QMetaObject.connectSlotsByName(resultwindow)

    def retranslateUi(self, resultwindow):
        _translate = QtCore.QCoreApplication.translate
        resultwindow.setWindowTitle(_translate("resultwindow", "MainWindow"))
        self.radioButton.setText(_translate("resultwindow", "RadioB&utton"))
        self.radioButton_2.setText(_translate("resultwindow", "RadioButton"))

