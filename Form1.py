# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(528, 315)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(250, 0, 20, 271))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.a_Label = QtWidgets.QLabel(self.centralwidget)
        self.a_Label.setGeometry(QtCore.QRect(110, 0, 31, 16))
        self.a_Label.setObjectName("a_Label")
        self.b_Label = QtWidgets.QLabel(self.centralwidget)
        self.b_Label.setGeometry(QtCore.QRect(380, 0, 31, 16))
        self.b_Label.setObjectName("b_Label")
        self.generate_Button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_Button.setGeometry(QtCore.QRect(90, 20, 75, 23))
        self.generate_Button.setObjectName("generate_Button")
        self.e_LineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.e_LineEdit2.setGeometry(QtCore.QRect(290, 40, 231, 20))
        self.e_LineEdit2.setReadOnly(True)
        self.e_LineEdit2.setObjectName("e_LineEdit2")
        self.ok_Label2 = QtWidgets.QLabel(self.centralwidget)
        self.ok_Label2.setGeometry(QtCore.QRect(370, 20, 47, 13))
        self.ok_Label2.setObjectName("ok_Label2")
        self.n_LineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.n_LineEdit2.setGeometry(QtCore.QRect(290, 70, 231, 20))
        self.n_LineEdit2.setReadOnly(True)
        self.n_LineEdit2.setObjectName("n_LineEdit2")
        self.d_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.d_LineEdit.setGeometry(QtCore.QRect(20, 150, 231, 20))
        self.d_LineEdit.setReadOnly(True)
        self.d_LineEdit.setObjectName("d_LineEdit")
        self.e_Label2 = QtWidgets.QLabel(self.centralwidget)
        self.e_Label2.setGeometry(QtCore.QRect(280, 40, 16, 16))
        self.e_Label2.setObjectName("e_Label2")
        self.n_Label2 = QtWidgets.QLabel(self.centralwidget)
        self.n_Label2.setGeometry(QtCore.QRect(280, 70, 16, 16))
        self.n_Label2.setObjectName("n_Label2")
        self.d_Label = QtWidgets.QLabel(self.centralwidget)
        self.d_Label.setGeometry(QtCore.QRect(10, 150, 16, 16))
        self.d_Label.setObjectName("d_Label")
        self.pk_Label = QtWidgets.QLabel(self.centralwidget)
        self.pk_Label.setGeometry(QtCore.QRect(100, 130, 61, 16))
        self.pk_Label.setObjectName("pk_Label")
        self.send_ok_Button = QtWidgets.QPushButton(self.centralwidget)
        self.send_ok_Button.setEnabled(False)
        self.send_ok_Button.setGeometry(QtCore.QRect(80, 180, 81, 23))
        self.send_ok_Button.setObjectName("send_ok_Button")
        self.r_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.r_LineEdit.setEnabled(False)
        self.r_LineEdit.setGeometry(QtCore.QRect(292, 120, 231, 20))
        self.r_LineEdit.setObjectName("r_LineEdit")
        self.text_Label = QtWidgets.QLabel(self.centralwidget)
        self.text_Label.setGeometry(QtCore.QRect(320, 100, 161, 16))
        self.text_Label.setObjectName("text_Label")
        self.r_Label = QtWidgets.QLabel(self.centralwidget)
        self.r_Label.setGeometry(QtCore.QRect(280, 120, 16, 16))
        self.r_Label.setObjectName("r_Label")
        self.e_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.e_LineEdit.setGeometry(QtCore.QRect(20, 70, 231, 20))
        self.e_LineEdit.setReadOnly(True)
        self.e_LineEdit.setObjectName("e_LineEdit")
        self.n_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.n_LineEdit.setGeometry(QtCore.QRect(20, 100, 231, 20))
        self.n_LineEdit.setReadOnly(True)
        self.n_LineEdit.setObjectName("n_LineEdit")
        self.n_Label = QtWidgets.QLabel(self.centralwidget)
        self.n_Label.setGeometry(QtCore.QRect(10, 100, 16, 16))
        self.n_Label.setObjectName("n_Label")
        self.ok_Label = QtWidgets.QLabel(self.centralwidget)
        self.ok_Label.setGeometry(QtCore.QRect(100, 50, 47, 13))
        self.ok_Label.setObjectName("ok_Label")
        self.e_Label = QtWidgets.QLabel(self.centralwidget)
        self.e_Label.setGeometry(QtCore.QRect(10, 70, 16, 16))
        self.e_Label.setObjectName("e_Label")
        self.send_r_Button = QtWidgets.QPushButton(self.centralwidget)
        self.send_r_Button.setGeometry(QtCore.QRect(360, 150, 75, 23))
        self.send_r_Button.setObjectName("send_r_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA"))
        self.a_Label.setText(_translate("MainWindow", "User A"))
        self.b_Label.setText(_translate("MainWindow", "User B"))
        self.generate_Button.setText(_translate("MainWindow", "Generate"))
        self.ok_Label2.setText(_translate("MainWindow", "Open key"))
        self.e_Label2.setText(_translate("MainWindow", "e"))
        self.n_Label2.setText(_translate("MainWindow", "n"))
        self.d_Label.setText(_translate("MainWindow", "d"))
        self.pk_Label.setText(_translate("MainWindow", "Private key"))
        self.send_ok_Button.setText(_translate("MainWindow", "Send open key"))
        self.text_Label.setText(_translate("MainWindow", "Enter number you want yo send"))
        self.r_Label.setText(_translate("MainWindow", "r"))
        self.n_Label.setText(_translate("MainWindow", "n"))
        self.ok_Label.setText(_translate("MainWindow", "Open key"))
        self.e_Label.setText(_translate("MainWindow", "e"))
        self.send_r_Button.setText(_translate("MainWindow", "Send"))
