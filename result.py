# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton

class Ui_ResultWindow(QMainWindow):
    def setupUi(self, ResultWindow):
        ResultWindow.setObjectName("ResultWindow")
        ResultWindow.resize(800, 600)
        ResultWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(ResultWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.space1 = QtWidgets.QLineEdit(self.centralwidget)
        self.space1.setGeometry(QtCore.QRect(160, 20, 113, 25))
        self.space1.setObjectName("space1")
        self.space2 = QtWidgets.QLineEdit(self.centralwidget)
        self.space2.setGeometry(QtCore.QRect(160, 50, 113, 25))
        self.space2.setObjectName("space2")
        self.space3 = QtWidgets.QLineEdit(self.centralwidget)
        self.space3.setGeometry(QtCore.QRect(160, 80, 113, 25))
        self.space3.setObjectName("space3")
        self.space4 = QtWidgets.QLineEdit(self.centralwidget)
        self.space4.setGeometry(QtCore.QRect(160, 110, 113, 25))
        self.space4.setObjectName("space4")
        self.space5 = QtWidgets.QLineEdit(self.centralwidget)
        self.space5.setGeometry(QtCore.QRect(160, 140, 113, 25))
        self.space5.setObjectName("space5")
        self.sub1 = QtWidgets.QLabel(self.centralwidget)
        self.sub1.setGeometry(QtCore.QRect(80, 30, 67, 17))
        self.sub1.setObjectName("sub1")
        self.sub2 = QtWidgets.QLabel(self.centralwidget)
        self.sub2.setGeometry(QtCore.QRect(80, 60, 67, 17))
        self.sub2.setObjectName("sub2")
        self.sub3 = QtWidgets.QLabel(self.centralwidget)
        self.sub3.setGeometry(QtCore.QRect(80, 90, 67, 17))
        self.sub3.setObjectName("sub3")
        self.sub4 = QtWidgets.QLabel(self.centralwidget)
        self.sub4.setGeometry(QtCore.QRect(80, 120, 67, 17))
        self.sub4.setObjectName("sub4")
        self.sub5 = QtWidgets.QLabel(self.centralwidget)
        self.sub5.setGeometry(QtCore.QRect(80, 150, 67, 17))
        self.sub5.setObjectName("sub5")
        self.clickingbelow = QtWidgets.QLabel(self.centralwidget)
        self.clickingbelow.setGeometry(QtCore.QRect(160, 210, 331, 61))
        self.clickingbelow.setObjectName("clickingbelow")
        self.result = QtWidgets.QPushButton(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(250, 270, 89, 25))
        self.result.setObjectName("result")
        pybutton.clicked.connect(self.giveAvg)

        def giveAvg(self):
            a=self.space1.text()
            b=self.space2.text()
            c=self.space3.text()
            d=self.space4.text()
            e=self.space5.text()      
        #msg.setIcon(QMessageBox)
               avg = (int(a)+int(b)+int(c)+int(d)+int(e))/5
               perct =float(avg)*100
               percentspace.setText("Your Percentage is" + perct)

    

        self.percentspace = QtWidgets.QTextEdit(self.centralwidget)
        self.percentspace.setGeometry(QtCore.QRect(10, 310, 571, 70))
        self.percentspace.setObjectName("percentspace")
        ResultWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ResultWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        ResultWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ResultWindow)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        ResultWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ResultWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultWindow)

    def retranslateUi(self, ResultWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultWindow.setWindowTitle(_translate("ResultWindow", "MainWindow"))
        self.sub1.setText(_translate("ResultWindow", "English"))
        self.sub2.setText(_translate("ResultWindow", "Hindi"))
        self.sub3.setText(_translate("ResultWindow", "Maths"))
        self.sub4.setText(_translate("ResultWindow", "Science"))
        self.sub5.setText(_translate("ResultWindow", "Computer"))
        self.clickingbelow.setText(_translate("ResultWindow", "Get Your Percentage By  Clicking Below"))
        self.result.setText(_translate("ResultWindow", "Get Result"))

 if name == 'main': 
     import sys app = QtWidgets,QApplication(sys.argv)
     minWin = ResultWindow
     minWin.show()
     sys.exit(app.exec_())