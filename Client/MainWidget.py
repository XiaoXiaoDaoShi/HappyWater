# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QThread,pyqtSignal

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 817)
        MainWindow.setMinimumSize(QtCore.QSize(550, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 10086))
        MainWindow.setWindowIcon(QtGui.QIcon('./pic/taiji.jpg'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_8.addWidget(self.line_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.topic_1 = QtWidgets.QLabel(self.centralwidget)
        self.topic_1.setScaledContents(True)
        self.topic_1.setAlignment(QtCore.Qt.AlignCenter)
        self.topic_1.setObjectName("topic_1")
        self.verticalLayout_5.addWidget(self.topic_1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 542, 219))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(200)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_8.addWidget(self.line)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_6.addWidget(self.line_3)
        self.topic_2 = QtWidgets.QLabel(self.centralwidget)
        self.topic_2.setAlignment(QtCore.Qt.AlignCenter)
        self.topic_2.setObjectName("topic_2")
        self.verticalLayout_6.addWidget(self.topic_2)
        self.forceAndBtnlLayout = QtWidgets.QHBoxLayout()
        self.forceAndBtnlLayout.setContentsMargins(-1, -1, 20, -1)
        self.forceAndBtnlLayout.setSpacing(20)
        self.forceAndBtnlLayout.setObjectName("forceAndBtnlLayout")
        self.forceLayout_3 = QtWidgets.QVBoxLayout()
        self.forceLayout_3.setObjectName("forceLayout_3")
        self.forceHlLayout_2 = QtWidgets.QHBoxLayout()
        self.forceHlLayout_2.setSpacing(0)
        self.forceHlLayout_2.setObjectName("forceHlLayout_2")
        self.forceLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.forceLabel_2.setStyleSheet("\n"
"font: 16pt \"隶书\";")
        self.forceLabel_2.setTextFormat(QtCore.Qt.AutoText)
        self.forceLabel_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.forceLabel_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.forceLabel_2.setObjectName("forceLabel_2")
        self.forceHlLayout_2.addWidget(self.forceLabel_2)
        self.forcNumberlabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.forcNumberlabel_2.setStyleSheet("font: 16pt \"Agency FB\";")
        self.forcNumberlabel_2.setObjectName("forcNumberlabel_2")
        self.forceHlLayout_2.addWidget(self.forcNumberlabel_2)
        self.forceHlLayout_2.setStretch(1, 1)
        self.forceLayout_3.addLayout(self.forceHlLayout_2)
        self.forceHlLayout = QtWidgets.QHBoxLayout()
        self.forceHlLayout.setSpacing(0)
        self.forceHlLayout.setObjectName("forceHlLayout")
        self.forceLabel = QtWidgets.QLabel(self.centralwidget)
        self.forceLabel.setStyleSheet("\n"
"font: 16pt \"隶书\";")
        self.forceLabel.setTextFormat(QtCore.Qt.AutoText)
        self.forceLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.forceLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.forceLabel.setObjectName("forceLabel")
        self.forceHlLayout.addWidget(self.forceLabel)
        self.forcNumberlabel = QtWidgets.QLabel(self.centralwidget)
        self.forcNumberlabel.setStyleSheet("font: 16pt \"Agency FB\";")
        self.forcNumberlabel.setObjectName("forcNumberlabel")
        self.forceHlLayout.addWidget(self.forcNumberlabel)
        self.forceHlLayout.setStretch(1, 1)
        self.forceLayout_3.addLayout(self.forceHlLayout)
        self.forceAndBtnlLayout.addLayout(self.forceLayout_3)
        self.breakthroughBtn = QtWidgets.QPushButton(self.centralwidget)
        self.breakthroughBtn.setStyleSheet("font: 16pt \"黑体\";\n"
"width:40%;\n"
"height:40%;")
        self.breakthroughBtn.setIconSize(QtCore.QSize(16, 16))
        self.breakthroughBtn.setAutoRepeat(False)
        self.breakthroughBtn.setAutoExclusive(True)
        self.breakthroughBtn.setAutoRepeatDelay(100)
        self.breakthroughBtn.setAutoDefault(False)
        self.breakthroughBtn.setDefault(False)
        self.breakthroughBtn.setFlat(False)
        self.breakthroughBtn.setObjectName("breakthroughBtn")
        self.forceAndBtnlLayout.addWidget(self.breakthroughBtn)
        self.verticalLayout_6.addLayout(self.forceAndBtnlLayout)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_8.addWidget(self.line_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_7.addWidget(self.line_4)
        self.topic_3 = QtWidgets.QLabel(self.centralwidget)
        self.topic_3.setAlignment(QtCore.Qt.AlignCenter)
        self.topic_3.setObjectName("topic_3")
        self.verticalLayout_7.addWidget(self.topic_3)
        self.guessAndBtnLayout = QtWidgets.QHBoxLayout()
        self.guessAndBtnLayout.setContentsMargins(0, 1, 20, 1)
        self.guessAndBtnLayout.setSpacing(20)
        self.guessAndBtnLayout.setObjectName("guessAndBtnLayout")
        self.guessHlLayout = QtWidgets.QHBoxLayout()
        self.guessHlLayout.setSpacing(0)
        self.guessHlLayout.setObjectName("guessHlLayout")
        self.guessLabel = QtWidgets.QLabel(self.centralwidget)
        self.guessLabel.setStyleSheet("\n"
"font: 16pt \"隶书\";")
        self.guessLabel.setTextFormat(QtCore.Qt.AutoText)
        self.guessLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.guessLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.guessLabel.setObjectName("guessLabel")
        self.guessHlLayout.addWidget(self.guessLabel)
        self.guessNumberlabel = QtWidgets.QLabel(self.centralwidget)
        self.guessNumberlabel.setStyleSheet("font: 16pt \"Agency FB\";")
        self.guessNumberlabel.setObjectName("guessNumberlabel")
        self.guessHlLayout.addWidget(self.guessNumberlabel)
        self.guessHlLayout.setStretch(1, 1)
        self.guessAndBtnLayout.addLayout(self.guessHlLayout)
        self.guessBtn = QtWidgets.QPushButton(self.centralwidget)
        self.guessBtn.setStyleSheet("font: 16pt \"华文行楷\";\n"
"width:40%;\n"
"height:40%;")
        self.guessBtn.setObjectName("guessBtn")
        self.guessAndBtnLayout.addWidget(self.guessBtn)
        self.guessAndBtnLayout.setStretch(0, 1)
        self.verticalLayout_7.addLayout(self.guessAndBtnLayout)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_8.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stateLabel = QtWidgets.QLabel(self.centralwidget)
        self.stateLabel.setObjectName("stateLabel")
        self.verticalLayout_4.addWidget(self.stateLabel)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./pic/stop.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout_4.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setStyleSheet("with:40%;\n"
"font: 16pt \"黑体\";\n"
"height:40%")
        self.startBtn.setObjectName("startBtn")
        self.verticalLayout_3.addWidget(self.startBtn)
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setStyleSheet("with:40%;\n"
"height:40%;\n"
"font: 16pt \"黑体\";")
        self.stopBtn.setIconSize(QtCore.QSize(16, 32))
        self.stopBtn.setObjectName("stopBtn")
        self.verticalLayout_3.addWidget(self.stopBtn)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.exitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitBtn.setStyleSheet("font: 16pt \"华文新魏\";")
        self.exitBtn.setObjectName("exitBtn")
        self.verticalLayout_8.addWidget(self.exitBtn)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_8.addWidget(self.line_7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.breakthroughBtn.clicked.connect(MainWindow.break_through)
        self.guessBtn.clicked.connect(MainWindow.guess)
        self.startBtn.clicked.connect(MainWindow.start_pratice)
        self.stopBtn.clicked.connect(MainWindow.stop_pratice)
        self.exitBtn.clicked.connect(MainWindow.exit_app)
        self.pushButton.clicked.connect(MainWindow.flush_ranking_list)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "佚名"))
        self.topic_1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">排行榜</span></p></body></html>"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "昵称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "原力值"))
        self.topic_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">消耗1000000000000000000（10^18)个原力碎片获取一点原力值</span></p></body></html>"))
        self.forceLabel_2.setText(_translate("MainWindow", "<html><head/><body><p>原力碎片：</p></body></html>"))
        self.forcNumberlabel_2.setText(_translate("MainWindow", "0"))
        self.forceLabel.setText(_translate("MainWindow", "原力："))
        self.forcNumberlabel.setText(_translate("MainWindow", "0"))
        self.breakthroughBtn.setText(_translate("MainWindow", "突破"))
        self.topic_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">消耗原力碎片，有概率获得原力值</span></p></body></html>"))
        self.guessLabel.setText(_translate("MainWindow", "<html><head/><body><p>氪金：</p></body></html>"))
        self.guessNumberlabel.setText(_translate("MainWindow", "0"))
        self.guessBtn.setText(_translate("MainWindow", "拼一把"))
        self.stateLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">休息中<span style=\" font-size:14pt;\">。。。</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "刷新排行榜"))
        self.startBtn.setText(_translate("MainWindow", "开始修炼"))
        self.stopBtn.setText(_translate("MainWindow", "结束修炼"))
        self.exitBtn.setText(_translate("MainWindow", "退出"))


class MainWidget(QMainWindow, Ui_MainWindow):

    def __init__(self, _control, _client):
        super().__init__()

        self.control = _control
        self.client = _client
        self.setupUi(self)
        self.initial(100)
        self.update_web_thread = UpdateWebThread(self.client, 10)
        self.update_web_thread.bind_singal(self.update_user_list)

        self.update_person_thread = UpdatePersonThread(self.control, 1)
        self.update_person_thread.bind_singal(self.update_force, self.update_force_debris, self.update_guess_number)

        self.update_web_thread.start()
        self.update_person_thread.start()

    def initial(self, _row_count):

        # 初始化 表格 排行榜
        self.tableWidget.setRowCount(_row_count)
        for i in range(_row_count):
            self.tableWidget.setItem(i, 0, QTableWidgetItem("暂无"))
            self.tableWidget.setItem(i, 1, QTableWidgetItem("0"))
        # 初始化 名字
        uaddress, uname, uforce = self.client.query_one(self.control.get_account())
        self.setWindowTitle("当前侠士--"+uname)

    def break_through(self):

        if self.control.get_balacne() >= 10**18:
            self.control.unlock_account()

            try:
                result = self.control.contract.gain_force(self.control.get_account(), self.control.get_balacne())
                QMessageBox.information(self, "Warning", "突破成功，消耗{}点原力碎片".format(result), QMessageBox.Yes)
            except:
                QMessageBox.information(self, "Warning", "不可抗力，无法突破", QMessageBox.Yes)
        else:
            reply = QMessageBox.information(self, "Warning", "你太弱了，无法突破", QMessageBox.Yes)

    def guess(self):
        if self.control.get_balacne() >= self.control.contract.get_guess_cost(self.control.get_account()):
            reply = QMessageBox.information(self, "Warning", "暂未开发。。", QMessageBox.Yes)

        else:
            reply = QMessageBox.information(self, "Warning", "你太穷了，拒绝你的氪金", QMessageBox.Yes)


    def flush_ranking_list(self):
        user_list = self.client.query_all()
        self.update_user_list(user_list)



    def start_pratice(self):
        self.label.setPixmap(QtGui.QPixmap("./pic/start.jpg"))
        self.stateLabel.setText(QtCore.QCoreApplication.translate("MainWindow",
                                           "<html><head/><body><p align=\"center\">修炼中<span style=\" font-size:14pt;\">。。。</span></p></body></html>"))
        self.control.start_work(1)

    def stop_pratice(self):
        self.label.setPixmap(QtGui.QPixmap("./pic/stop.jpg"))
        self.stateLabel.setText(QtCore.QCoreApplication.translate("MainWindow",
                                                                  "<html><head/><body><p align=\"center\">休息中<span style=\" font-size:14pt;\">。。。</span></p></body></html>"))
        self.control.stop_work()

    def exit_app(self):
        self.client.close()
        self.control.stop_work()
        try:
            self.control.geth_stop_2()
        except:
            try:
                self.control.geth_stop()
            except:
                pass

        if not self.control.is_connected():
            try:
                self.control.geth_stop_2()
            except:
                try:
                    self.control.geth_stop()
                except:
                    pass
        self.close()

    def update_force(self, _force):
        # 通过信号更新 force值 str
        self.forcNumberlabel.setText(_force)
        try:
            self.client.update_force(self.control.get_account(), _force)
        except:
            pass

    def update_force_debris(self, _force_debris):
        # 跟新force 碎片 str
        self.forcNumberlabel_2.setText(_force_debris)

    def update_user_list(self, _user_list):
        # 跟新排行榜 list[]
        row_count = len(_user_list)
        for i in range(row_count):
            name, force_number = _user_list[i]  # 名字， 原力值
            self.tableWidget.setItem(i, 0,QTableWidgetItem(name))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(force_number)))

    def update_guess_number(self, _number):
        # 更新 氪金数量 str
        self.guessNumberlabel.setText(_number)



class UpdatePersonThread(QThread):
    """
    更新个人数据
    force force碎片 氪金数
    """
    # force 信号 传入 str
    force_singal = pyqtSignal(str)
    force_debris_singal = pyqtSignal(str)           # force 碎片
    guess_number_singal = pyqtSignal(str)                  # 氪金 数


    def __init__(self, _control, _interval):
        """

        :param _control:
        :param _interval:   更新间隔 s
        """
        super().__init__()
        self.control = _control
        self.interval = _interval

    def bind_singal(self, _update_force, _update_force_debris, _update_guess_number):
        self.force_singal.connect(_update_force)
        self.force_debris_singal.connect(_update_force_debris)
        self.guess_number_singal.connect(_update_guess_number)

    def run(self):
        account = self.control.get_account()
        while True:
            try:
                my_force = self.control.contract.get_my_force(account) # 获得当前账户的 force
                guess_number = self.control.contract.get_guess_cost(account) # 获得当前账户的氪金数
                force_debris = self.control.get_balacne() # 获得force碎片
                self.force_singal.emit(str(my_force))
                self.force_debris_singal.emit(str(force_debris))
                self.guess_number_singal.emit(str(guess_number))

            except:
                pass
            self.sleep(self.interval)


class UpdateWebThread(QThread):
    """
    同步网络数据
    """
    user_list_singal = pyqtSignal(list) # user 列表 用于更新排行榜

    def __init__(self, _client, _interval):
        super().__init__()
        self.client = _client
        self.interval = _interval

    def bind_singal(self, _update_user_list):
        self.user_list_singal.connect(_update_user_list)

    def run(self):
        while True:
            try:
                user_list = self.client.query_all()
                if user_list !=None:
                    self.user_list_singal.emit(user_list)
                    self.sleep(self.interval)
            except:
                pass





