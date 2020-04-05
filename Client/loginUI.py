# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QMainWindow
from Happy.Client.MainWidget import MainWidget
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 350)
        MainWindow.setMinimumSize(QtCore.QSize(350, 350))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.loginPasswd = QtWidgets.QLineEdit(self.centralwidget)
        self.loginPasswd.setStyleSheet("font: 12pt \"Agency FB\";\n"
"")
        self.loginPasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginPasswd.setObjectName("loginPasswd")
        self.verticalLayout_2.addWidget(self.loginPasswd)
        self.loginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginBtn.setStyleSheet("font: 14pt \"黑体\";")
        self.loginBtn.setObjectName("loginBtn")
        self.verticalLayout_2.addWidget(self.loginBtn)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.registerName = QtWidgets.QLineEdit(self.centralwidget)
        self.registerName.setStyleSheet("font: 14pt \"楷体\";")
        self.registerName.setObjectName("registerName")
        self.horizontalLayout.addWidget(self.registerName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.registerPasswd = QtWidgets.QLineEdit(self.centralwidget)
        self.registerPasswd.setStyleSheet("font: 14pt \"楷体\";")
        self.registerPasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.registerPasswd.setObjectName("registerPasswd")
        self.horizontalLayout_2.addWidget(self.registerPasswd)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.registerPasswd_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.registerPasswd_2.setStyleSheet("font: 14pt \"楷体\";")
        self.registerPasswd_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.registerPasswd_2.setObjectName("registerPasswd_2")
        self.horizontalLayout_3.addWidget(self.registerPasswd_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.registerBtn = QtWidgets.QPushButton(self.centralwidget)
        self.registerBtn.setStyleSheet("font: 11pt \"隶书\";")
        self.registerBtn.setObjectName("registerBtn")
        self.verticalLayout.addWidget(self.registerBtn)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.loginBtn.clicked.connect(self.login_in)
        self.registerBtn.clicked.connect(self.register)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "start"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">输入密码即可登录</span></p></body></html>"))
        self.loginBtn.setText(_translate("MainWindow", "登录"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">输入你的大侠名和密码即可注册</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">名称：</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">密码：</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">重复密码：</span></p></body></html>"))
        self.registerBtn.setText(_translate("MainWindow", "注册"))


class LoingUI(QMainWindow,Ui_MainWindow):
    def __init__(self, _control, _client):
        super().__init__()

        self.control = _control
        self.clinet = _client
        self.setupUi(self)
    window_list = []

    def login_in(self):
        if self.loginPasswd.text() == None:
            reply = QMessageBox.information(self, "Warning", "密码为空", QMessageBox.Yes)
        else:
            if os.path.exists("./account") :
                with open("./account", "rb") as f:
                    account = f.read().decode()

                self.control.set_account(account)
                self.control.set_passwd(self.loginPasswd.text())

                result = self.control.unlock_account()

                if result:
                    # 登录成功
                    self.control.set_coinbase(account)

                    QMessageBox.information(self, "Warning", "欢迎回来", QMessageBox.Yes)
                    self.control.set_passwd(self.loginPasswd.text())
                    self.control.set_account(account)

                    main_window = MainWidget(self.control,self.clinet)

                    self.window_list.append(main_window)
                    self.close()
                    main_window.show()
                else:
                    QMessageBox.information(self, "Warning", "密码错误", QMessageBox.Yes)
            else:
                reply = QMessageBox.information(self, "Warning", "未发现身份", QMessageBox.Yes)


    def register(self):
        """
        注册一个账户
        :return:
        """
        if self.registerPasswd.text() != self.registerPasswd_2.text():
            reply = QMessageBox.information(self,"Warning","两次密码输入不一致",QMessageBox.Yes)

        elif self.registerName.text() == None:
            reply = QMessageBox.information(self, "Warning", "用户名为空", QMessageBox.Yes)

        else:
            account = self.control.new_account(self.registerPasswd.text())
            result = self.clinet.insert_one(account, self.registerName.text())

            if result > 0 :
                reply = QMessageBox.information(self, "Warning", "注册成功", QMessageBox.Yes)
                with open("./account", "wb") as f:
                    f.write(account.encode())
            else:
                reply = QMessageBox.information(self, "Warning", "注册失败", QMessageBox.Yes)
