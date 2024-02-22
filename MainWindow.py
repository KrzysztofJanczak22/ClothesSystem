from PyQt5 import QtCore, QtGui, QtWidgets
from DialogClothes import Ui_Dialog_Clothes

class Ui_MainWindow(object):

    def openWindow_DialogClothes(self):
        self.window_Clothes = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_Clothes()
        self.ui.setupUi(self.window_Clothes)
        self.window_Clothes.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 791, 521))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(810, 50, 160, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_OpenClothes = QtWidgets.QPushButton(self.verticalLayoutWidget, clicked = lambda: self.openWindow_DialogClothes())
        self.pushButton_OpenClothes.setObjectName("pushButton_OpenClothes")
        self.verticalLayout_2.addWidget(self.pushButton_OpenClothes)
        self.pushButton_EndJob = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_EndJob.setObjectName("pushButton_EndJob")
        self.verticalLayout_2.addWidget(self.pushButton_EndJob)
        self.pushButton_CancelJob = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_CancelJob.setObjectName("pushButton_CancelJob")
        self.verticalLayout_2.addWidget(self.pushButton_CancelJob)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 961, 31))
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
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.pushButton_Search = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.horizontalLayout.addWidget(self.pushButton_Search)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_OpenClothes.setText(_translate("MainWindow", "Ubrania"))
        self.pushButton_EndJob.setText(_translate("MainWindow", "Zakończ zlecenie"))
        self.pushButton_CancelJob.setText(_translate("MainWindow", "Odrzuć zlecenie"))
        self.label_FirstName.setText(_translate("MainWindow", "Imię:"))
        self.label_2.setText(_translate("MainWindow", "Nazwisko:"))
        self.pushButton_Search.setText(_translate("MainWindow", "Szukaj"))



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        pass