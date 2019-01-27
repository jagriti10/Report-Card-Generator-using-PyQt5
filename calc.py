# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Ui_form(object):
    def addition(self):
        a =self.Num1.text()
        b=self.num2.text()
        z =int(a)+int(b)
        msg=QMessageBox()
        #msg.setIcon(QMessageBox)
        msg.setText(str(z))
        msg.setWindowTitle("Result")
        msg.exec()
    def subtract(self):
        a =self.Num1.text()
        b=self.num2.text()
        z =int(a)-int(b)
        msg=QMessageBox()
        #msg.setIcon(QMessageBox)
        msg.setText(str(z))
        msg.setWindowTitle("Result")
        msg.exec()
    def multiply(self):
        a =self.Num1.text()
        b=self.num2.text()
        z =int(a)*int(b)
        msg=QMessageBox()
        #msg.setIcon(QMessageBox)
        msg.setText(str(z))
        msg.setWindowTitle("Result")
        msg.exec()
    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(486, 574)
        self.Num1 = QtWidgets.QLineEdit(form)
        self.Num1.setGeometry(QtCore.QRect(20, 50, 241, 34))
        self.Num1.setObjectName("Num1")
        self.num2 = QtWidgets.QLineEdit(form)
        self.num2.setGeometry(QtCore.QRect(20, 120, 241, 34))
        self.num2.setObjectName("num2")
        self.ADD = QtWidgets.QPushButton(form)
        self.ADD.setGeometry(QtCore.QRect(40, 220, 103, 34))
        self.ADD.setObjectName("ADD")
        self.ADD.clicked.connect(self.addition)
        self.pushButton = QtWidgets.QPushButton(form)
        self.pushButton.setGeometry(QtCore.QRect(180, 220, 103, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.subtract)
        self.pushButton_2 = QtWidgets.QPushButton(form)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 220, 103, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.multiply)

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "Dialog"))
        self.ADD.setText(_translate("form", "ADD"))
        self.pushButton.setText(_translate("form", "SUB"))
        self.pushButton_2.setText(_translate("form", "MUL"))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

