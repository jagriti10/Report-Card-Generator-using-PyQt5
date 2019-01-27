# Project-1-PyQt5
This is a try project developed on PyQt5 .
The command used to execute .py document :- 
if __name__ == '__main__':
    import sys
    app = QtWidgets,QApplication(sys.argv);
    Dialog = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setUpUi(Dialog)
    Dialog.shoW()
    sys.exit(app.exec_())
