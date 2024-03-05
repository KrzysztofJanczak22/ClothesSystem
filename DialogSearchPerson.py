from PyQt5 import QtCore, QtGui, QtWidgets
import Background_MainWindow

class Ui_Dialog(object):

    def fn_AssignClothToEmployee(self):
        from DialogClothes import v_idcloth
        v_idemployee = self.fn_GetIDEmployee()
        print(v_idcloth,v_idemployee)
        Background_MainWindow.fn_AssignCloth(v_idcloth,v_idemployee)
    def fn_EmployeeToList(self):
        self.listWidget.clear()
        v_firstname = self.lineEdit_FirstName.text()
        v_lastname = self.lineEdit_LastName.text()
        results = Background_MainWindow.fn_GetListEmployee(v_firstname,v_lastname)
        for employee in results:
            text = f'{employee[0]}: {employee[1]} {employee[2]}'
            self.listWidget.addItem(text)
    def fn_GetIDEmployee(self):
        text = self.listWidget.currentItem().text()
        text = text.split(':')
        v_idemployee = text[0]
        return v_idemployee

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(515, 322)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 61, 491, 211))
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 491, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_FirstName = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_FirstName.setObjectName("label_FirstName")
        self.horizontalLayout.addWidget(self.label_FirstName)
        self.lineEdit_FirstName = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_FirstName.setObjectName("lineEdit_FirstName")
        self.horizontalLayout.addWidget(self.lineEdit_FirstName)
        self.label_LastName = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_LastName.setObjectName("label_LastName")
        self.horizontalLayout.addWidget(self.label_LastName)
        self.lineEdit_LastName = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_LastName.setObjectName("lineEdit_LastName")
        self.horizontalLayout.addWidget(self.lineEdit_LastName)
        self.pushButton_Search = QtWidgets.QPushButton(self.horizontalLayoutWidget, clicked = lambda: self.fn_EmployeeToList())
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.horizontalLayout.addWidget(self.pushButton_Search)
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.fn_AssignClothToEmployee())
        self.pushButton.setGeometry(QtCore.QRect(390, 280, 111, 28))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_FirstName.setText(_translate("Dialog", "Imię:"))
        self.label_LastName.setText(_translate("Dialog", "Nazwisko:"))
        self.pushButton_Search.setText(_translate("Dialog", "Szukaj"))
        self.pushButton.setText(_translate("Dialog", "Potwierdz"))



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window_SearchPerson = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(window_SearchPerson)
    window_SearchPerson.show()

    sys.exit(app.exec_())