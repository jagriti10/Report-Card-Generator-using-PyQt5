# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class sign(object):
    def showme(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()
    
    def setupUi(self,Form):
        #name =self.lineEdit.text()
        #uname =self.lineEdit_2.text()
        #pswrd =self.lineEdit_3.text()
        Form.setObjectName("Form")
        Form.resize(739, 525)
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(90, 120, 67, 17))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(90, 180, 67, 17))
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(Form)
        self.label3.setGeometry(QtCore.QRect(90, 240, 67, 17))
        self.label3.setObjectName("label3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 110, 471, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 170, 471, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 240, 471, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.signB = QtWidgets.QPushButton(Form)
        self.signB.setGeometry(QtCore.QRect(280, 360, 89, 25))
        self.signB.setObjectName("signB")
        self.signB.clicked.connect(self.showme)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self,Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label1.setText(_translate("Form", "Name"))
        self.label2.setText(_translate("Form", "Username"))
        self.label3.setText(_translate("Form", "Password"))
        self.signB.setText(_translate("Form", "Sign Up"))

class hello(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.labelF2 = QtWidgets.QLabel(Form)
        self.labelF2.setGeometry(QtCore.QRect(50, 80, 271, 20))
        self.labelF2.setObjectName("labelF2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelF2.setText(_translate("Form", "HELLO"))

class Ui_Form(object):
    def showme(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = hello()
        self.ui.setupUi(self.window)
        Dialog.hide()
        self.window.show()
    def auth(self):
        user =self.lineEdit.text()
        passw =self.lineEdit_2.text()
        u ='jagriti'
        p='jagriti'
        if(user == u):
            self.showme()
        else:
            print ("User not found")    
    def setupUi(self,Form):
        Form.setObjectName("Form")
        Form.resize(775, 394)
        self.loginB = QtWidgets.QPushButton(Form)
        self.loginB.setGeometry(QtCore.QRect(200, 280, 89, 25))
        self.loginB.setObjectName("loginB")
        self.loginB.clicked.connect(self.auth)
        self.cancelB = QtWidgets.QPushButton(Form)
        self.cancelB.setGeometry(QtCore.QRect(420, 280, 89, 25))
        self.cancelB.setObjectName("cancelB")
        self.labet1 = QtWidgets.QLabel(Form)
        self.labet1.setGeometry(QtCore.QRect(60, 70, 67, 17))
        self.labet1.setObjectName("labet1")
        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(60, 150, 67, 17))
        self.label2.setObjectName("label2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 60, 511, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 140, 511, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.loginB.setText(_translate("Form", "login"))
        self.cancelB.setText(_translate("Form", "Cancel"))
        self.labet1.setText(_translate("Form", "Username"))
        self.label2.setText(_translate("Form", "Password"))





if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = sign()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

