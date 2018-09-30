# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knight.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from main import runcrawler

class Ui_MainWindow(object):
    def crawler(self):
        pro = self.lineEdit_project.text()
        url = self.lineEdit_url.text()
        runcrawler(pro,url)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.icon = QtWidgets.QLabel(self.centralwidget)
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("icon/logo.png"))
        self.icon.setAlignment(QtCore.Qt.AlignCenter)
        self.icon.setObjectName("icon")
        self.verticalLayout.addWidget(self.icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_project = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_project.setObjectName("lineEdit_project")
        self.horizontalLayout.addWidget(self.lineEdit_project)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_url = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.horizontalLayout_2.addWidget(self.lineEdit_url)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.go = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/Cute-Ball-Go-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.go.setIcon(icon)
        self.go.setObjectName("go")
        self.go.clicked.connect(self.crawler)
        self.horizontalLayout_3.addWidget(self.go)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCrwaled = QtWidgets.QAction(MainWindow)
        self.actionCrwaled.setObjectName("actionCrwaled")
        self.actionQueued = QtWidgets.QAction(MainWindow)
        self.actionQueued.setObjectName("actionQueued")
        self.menubar.addAction(self.menuFiles.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Project name"))
        self.label_2.setText(_translate("MainWindow", "Url :"))
        self.go.setText(_translate("MainWindow", "GO"))
        self.menuFiles.setTitle(_translate("MainWindow", "KNIGHT"))
        self.actionCrwaled.setText(_translate("MainWindow", "Crwaled"))
        self.actionQueued.setText(_translate("MainWindow", "Queued"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

