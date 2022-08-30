import paramiko
import time
import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1032, 768 )
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 211, 641))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.horizontalLayoutWidget)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(230, 10, 781, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(220, 10, 17, 639))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(240, 610, 561, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(804, 610, 101, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(910, 610, 101, 41))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(240, 650, 771, 71))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget_5)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_3.setGeometry(QtCore.QRect(0, 8, 473, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_5.setGeometry(QtCore.QRect(482, 6, 75, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_2.setGeometry(QtCore.QRect(2, 8, 473, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_4.setGeometry(QtCore.QRect(482, 6, 75, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_6, "")
        self.verticalLayout_6.addWidget(self.tabWidget)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(118, 692, 89, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 692, 89, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(12, 660, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuLog = QtWidgets.QMenu(self.menubar)
        self.menuLog.setObjectName("menuLog")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuLog.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ScriptingSSH"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Switches"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Группа 1"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "host"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "host"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "host"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Группа 2"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "host"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "Группа 3"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "host"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.pushButton_2.setText(_translate("MainWindow", "Recive"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Команда 1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Команда 2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Команда 3"))
        self.pushButton_5.setText(_translate("MainWindow", "Send"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Commands"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Скрипт 1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Скрипт 2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Скрипт 3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Скрипт 4"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Скрипт 5"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Скрипт 6"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Скрипт 7"))
        self.pushButton_4.setText(_translate("MainWindow", "Start script"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Scripts"))
        self.pushButton_3.setText(_translate("MainWindow", "Dissconect"))
        self.pushButton_6.setText(_translate("MainWindow", "Connect"))
        self.label.setText(_translate("MainWindow", "Двойной клик по Switch"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Settings"))
        self.menuLog.setTitle(_translate("MainWindow", "Log"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))


        def clicked(): #для корректной работы  pushButton_6.clicked.connect нужна эта функция
            #ssh().connection() #зaпускает ссесию SSH
            self.textBrowser.append(ssh().connection())#получает строку которая возвращет ф-уя ssh
        self.pushButton_6.clicked.connect(clicked)  # кнопка запускает функциию connection для открытия SSH канала



        self.treeWidget.doubleClicked.connect(self.getValue) #отправляет сигнал в функцию из QTree в QLabel, выбраный свитч по двоеному нажатию
    def getValue(self, par1): # фунуция для заполнения Qlabel
        self.label.setText(par1.data())  #подставляет выбраный свитч в Qlabel
        #print(par1.row()) #
        #print(par1.column()) #колонка



class ssh():
    def __init__(self):
       self.host = 'tty.sdf.org'  # Remote device we want to interact with
       self.user = 'alekseyla5'  # SSH user
       self.passw = '4SfjGDjNiMGbBA'  # SSH passwor
       self.ssh = paramiko.SSHClient()

    def sendcommand(self):
      self.channel.send("com" + "\n")
      time.sleep(1)
      output = self.channel.recv(999999)
      print(output.decode())
      print('333')
      return output.decode()


    def connection(self):
     try:
       self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       self.ssh.connect(hostname=self.host, username=self.user, password=self.passw, look_for_keys=False, allow_agent=False) #look_for_keys - ключт при первом конекте, allow_agent встроенный агент SSh
       self.channel = self.ssh.invoke_shell()# на каком то оборудование работает invoke_shell на каком то exec_command, зависит от типа канала который поддерживает сервер
     except:
       print ("Login to {} failed".format(self.host))
       self.channel = False
     if self.channel:
        self.channel.send("" + "\n")
        self.channel.send("" + "\n")
        self.channel.send("" + "\n")
        time.sleep(1)
        output = self.channel.recv(99999)
        print(output.decode())


        #ssh.close()
     else:
        print ("Sorry, there is no connection to the host {}".format(self.host))
     return output.decode()

#блок кода запустится если интерпретатор данный фаил будет выполнять как осн. программу и присвоит спец переменой  __name__  имя __main__
if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  MainWindow = QtWidgets.QMainWindow()
  ui = Ui_MainWindow()
  ui.setupUi(MainWindow)
  MainWindow.show()
  sys.exit(app.exec_()) #запускает основной цикл и возвращает код состояния


from PyQt5 import QtCore, QtWidgets

class MyThread(QtCore.QThread):
      mysignal = QtCore.pyqtSignal(str)
      def __init__(self, parent=None):
          QtCore.QThread.__init__(self, parent)
          self.running = False # Флаг выполнения
          self.count = 0
      def run(self):
          self.running = True
          while self.running:	# Проверяем значение флага
                self.count += 1
                self.mysignal.emit("count = %s" % self.count)
                self.sleep(1)	# Имитируем процесс

class MyWindow(QtWidgets.QWidget):
      def __init__(self, parent=None):
          QtWidgets.QWidget.__init__(self, parent)
          self.label = QtWidgets.QLabel("Нажмите кнопку для запуска потока")
          self.label.setAlignment(QtCore.Qt.AlignHCenter)
          self.btnStart = QtWidgets.QPushButton("Запустить поток")
          self.btnStop = QtWidgets.QPushButton("Остановить поток")
          self.vbox = QtWidgets.QVBoxLayout()
          self.vbox.addWidget(self.label)
          self.vbox.addWidget(self.btnStart)
          self.vbox.addWidget(self.btnStop)
          self.setLayout(self.vbox)
          self.mythread = MyThread()
          self.btnStart.clicked.connect(self.on_start)
          self.btnStop.clicked.connect(self.on_stop)
          self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)
      def on_start(self):
          if not self.mythread.isRunning():
                 self.mythread.start()	# Запускаем поток
      def on_stop(self):
          self.mythread.running = False # Изменяем флаг выполнения
      def on_change(self, s):
          self.label.setText(s)
      def closeEvent(self, event):	# Вызывается при закрытии окна
          self.hide()	# Скрываем окно
          self.mythread.running = False # Изменяем флаг выполнения
          self.mythread.wait(5000)	# Даем время, чтобы закончить
          event.accept()	# Закрываем окно
if __name__ == "__main__" :
  import sys
  app = QtWidgets.QApplication(sys.argv)
  window = MyWindow()
  window.setWindowTitle("Запуск и остановка потока")
  window.resize(300, 100)
  window.show()
  sys.exit(app.exec_())

# coding: utf-8
from PyQt5 import QtCore, QtWidgets


class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
    def run(self):
        for i in range(1, 21):
          self.sleep(3) # "Засыпаем" на 3 секунды # Передача данных из потока через сигнал
          self.mysignal.emit("i = %s" % i)

class MyWindow(QtWidgets.QWidget) :
    def __init__(self, parent=None) :
       QtWidgets.QWidget.__init__(self, parent)
       self.label = QtWidgets.QLabel("Нажмите кнопку для запуска потока")
       self.label.setAlignment(QtCore.Qt.AlignHCenter)
       self.button = QtWidgets.QPushButton("Запустить процесс")
       self.vbox = QtWidgets.QVBoxLayout()
       self.vbox.addWidget(self.label)
       self.vbox.addWidget(self.button)
       self.setLayout(self.vbox)
       self.mythread = MyThread() # Создаем экземпляр класса
       self.button.clicked.connect(self.on_clicked)
       self.mythread.started.connect(self.on_started)
       self.mythread.finished.connect(self.on_finished)
       self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)

    def on_clicked(self):
        self.button.setDisabled(True)  # Делаем кнопку неактивной
        self.mythread.start()  # Запускаем поток
    def on_started(self):  # Вызывается при запуске потока
        self.label.setText("Вызван метод on_started()")
    def on_finished(self):  # Вызывается при завершении потока
        self.label.setText("Вызван метод on_finished()")
        self.button.setDisabled(False)  # Делаем кнопку активной
    def on_change(self, s):
        self.label.setText(s)

if  __name__ == "__main__" :
   import sys
   app = QtWidgets.QApplication(sys.argv)
   window = MyWindow()
   window.setWindowTitle("Использование класса QThread")
   window.resize(300, 70)
   window.show()
   sys.exit(app.exec_())

# coding: utf-8
from PyQt5 import QtCore, QtWidgets


class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
    def run(self):
        for i in range(1, 21):
          self.sleep(3) # "Засыпаем" на 3 секунды # Передача данных из потока через сигнал
          self.mysignal.emit("i = %s" % i)

class MyWindow(QtWidgets.QWidget) :
    def __init__(self, parent=None) :
       QtWidgets.QWidget.__init__(self, parent)
       self.label = QtWidgets.QLabel("Нажмите кнопку для запуска потока")
       self.label.setAlignment(QtCore.Qt.AlignHCenter)
       self.button = QtWidgets.QPushButton("Запустить процесс")
       self.vbox = QtWidgets.QVBoxLayout()
       self.vbox.addWidget(self.label)
       self.vbox.addWidget(self.button)
       self.setLayout(self.vbox)
       self.mythread = MyThread() # Создаем экземпляр класса
       self.button.clicked.connect(self.on_clicked)
       self.mythread.started.connect(self.on_started)
       self.mythread.finished.connect(self.on_finished)
       self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)

    def on_clicked(self):
        self.button.setDisabled(True)  # Делаем кнопку неактивной
        self.mythread.start()  # Запускаем поток
    def on_started(self):  # Вызывается при запуске потока
        self.label.setText("Вызван метод on_started()")
    def on_finished(self):  # Вызывается при завершении потока
        self.label.setText("Вызван метод on_finished()")
        self.button.setDisabled(False)  # Делаем кнопку активной
    def on_change(self, s):
        self.label.setText(s)

if  __name__ == "__main__" :
   import sys
   app = QtWidgets.QApplication(sys.argv)
   window = MyWindow()
   window.setWindowTitle("Использование класса QThread")
   window.resize(300, 70)
   window.show()
   sys.exit(app.exec_())

import sys
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QColor


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(453, 408)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Example"))
        self.pushButton.setText(_translate("Form", "Input"))


# клаас в виде объекта, который будет перенесён в другой поток для выполнения кода, наследуется от QtCore.QObject
class BrowserHandler(QtCore.QObject):
    running = False
    newTextAndColor = QtCore.pyqtSignal(str, object) #создаем атребут и заносим в него значение возвращенное методом pyqtSignal(str, object)

    # метод, который будет выполнять алгоритм в другом потоке
    def run(self):
        while True:
            # посылаем сигнал из второго потока в GUI поток
            self.newTextAndColor.emit('{} - thread 2 variant 1.\n'.format(str(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))),
                QColor(0, 0, 255))
            QtCore.QThread.msleep(1000)

            # посылаем сигнал из второго потока в GUI поток
            self.newTextAndColor.emit('{} - thread 2 variant 2.\n'.format(str(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))),
                QColor(255, 0, 0))
            QtCore.QThread.msleep(1000)


class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__() #позволяет работать с атрибутами класса родителя
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # используем кнопку для добавления текста с цветом в главном потоке
        self.ui.pushButton.clicked.connect(self.addAnotherTextAndColor)

        # создадим поток
        self.thread = QtCore.QThread()
        # создадим объект для выполнения кода в другом потоке
        self.browserHandler = BrowserHandler()
        # перенесём объект в другой поток
        self.browserHandler.moveToThread(self.thread)
        # после чего подключим все сигналы и слоты
        self.browserHandler.newTextAndColor.connect(self.addNewTextAndColor)
        # подключим сигнал старта потока к методу run у объекта, который должен выполнять код в другом потоке
        self.thread.started.connect(self.browserHandler.run)
        # запустим поток
        self.thread.start()

    @QtCore.pyqtSlot(str, object)
    def addNewTextAndColor(self, string, color):
        self.ui.textBrowser.setTextColor(color)
        self.ui.textBrowser.append(string)

    def addAnotherTextAndColor(self):
        self.ui.textBrowser.setTextColor(QColor(0, 255, 0))
        self.ui.textBrowser.append(
            '{} - thread 2 variant 3.\n'.format(str(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime()))))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())



import sys
import time
import paramiko
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QColor



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(453, 408)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Example"))
        self.pushButton.setText(_translate("Form", "Input"))


# клаас в виде объекта, который будет перенесён в другой поток для выполнения кода, наследуется от QtCore.QObject
class startSshSesion(QtCore.QObject):
    strSshOutput = QtCore.pyqtSignal(str) #создаем атрибут и заносим в него значение возвращенное методом pyqtSignal(str, object)

    # метод, который будет выполнять алгоритм в другом потоке
    def run(self):
      try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname="tty.sdf.org", port=22, username='alekseyla5', password='4SfjGDjNiMGbBA', look_for_keys=False, timeout=None)
        connection = ssh.invoke_shell()
        while True:
           # command = input('Нажми Enter')
            #if command == 'exit':
                #break
            connection.send("\n")
            #if connection.recv_ready():
            output = connection.recv(9999).decode(encoding='utf-8')
               #if len(output) != "":
            print(output)
            self.strSshOutput.emit(output)
            QtCore.QThread.msleep(2000)
      except paramiko.AuthenticationException:
          print("User or password incorrect, Please try again!!!")


class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__() #позволяет работать с атрибутами класса родителя
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # используем кнопку для добавления текста  в главном потоке
        self.ui.pushButton.clicked.connect(self.sendSshCommand)
        # создадим поток
        self.thread = QtCore.QThread()
        # создадим объект для выполнения кода в другом потоке
        self.startSsh = startSshSesion() #ссылаемся на созданый класс
        # перенесём объект в другой поток
        self.startSsh.moveToThread(self.thread)
        # после чего подключим все сигналы и слоты
        self.startSsh.strSshOutput.connect(self.printSshOutput)
        # подключим сигнал старта потока к методу run у объекта, который должен выполнять код в другом потоке
        self.thread.started.connect(self.startSsh.run)
        # запустим поток
        self.thread.start()

    @QtCore.pyqtSlot(str)
    def printSshOutput(self, string):
        self.ui.textBrowser.append(string)

    def sendSshCommand(self):
        self.ui.textBrowser.append('{} - thread 2 variant 3.\n')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())



import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 110, 500, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 50, 50, 20))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 220, 150, 43))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    finished = QtCore.pyqtSignal()

    def __init__(self ):
        super(MyThread, self).__init__()
        self.text = "__init__"                                                # +++

    def run(self):
        for i in range(1, 40):           # Какой-то цикл
            QtCore.QThread.msleep(1000)
            self.mysignal.emit("Поток работает: i = {} <-> {}".format(i, self.text))
        self.finished.emit()

class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.setText("Запустить поток")
        self.pushButton.clicked.connect(self.func1)
# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        self.lineEdit.setPlaceholderText("Напишите здесь текст и нахмите "
                                         "`Enter` для передачи текста в поток.")
        self.lineEdit.setToolTip("press RETURN to send")
        self.lineEdit.setStyleSheet("""
            QLineEdit {
               border: None;
               font-size: 14px;
               }
               """)
        self.lineEdit.returnPressed.connect(self.sendText)
# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    def func1(self):
        self.thread = MyThread()
        self.thread.mysignal.connect(self.on_change, type=QtCore.Qt.QueuedConnection)
        self.thread.finished.connect(self.on_finished)
        self.thread.start()

    def on_change(self, s):
        self.label.setText(s)
        self.label.adjustSize()

# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    def sendText(self):
        self.thread.text = self.lineEdit.text()

    @QtCore.pyqtSlot()
    def on_finished(self):
        s = self.label.text().replace("Поток работает", "Поток завершил работу")
        self.label.setText(s)
# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

import paramiko
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, QThreadPool, QRunnable, pyqtSignal, pyqtSlot, QObject


class SSHWorkerSignals(QObject):
    result = pyqtSignal('PyQt_PyObject', 'PyQt_PyObject')


class SSHWorker(QRunnable):
    def __init__(self):
        super(SSHWorker, self).__init__()
        self.ssh_signals = SSHWorkerSignals()
        self.ssh_server = 'test.server.corp'

    @pyqtSlot()
    def run(self):
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.load_system_host_keys()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            ssh_client.connect(self.ssh_server, port=22, username='test', password='test')
            stdin, stdout, stderr = ssh_client.exec_command('uname -a')
            std_out = str(stdout.read())
            self.ssh_signals.result.emit(self.ssh_server, std_out)
        except Exception as e:
            self.ssh_signals.result.emit(self.ssh_server, str(e))
        finally:
            ssh_client.close()


class CompareWorker(QObject):
    done = pyqtSignal()

    def __init__(self):
        super(CompareWorker, self).__init__()
        self.ssh_threadpool = QThreadPool()
        self.ssh_threadpool.setMaxThreadCount(10)

    @pyqtSlot()
    def execute(self):
        ssh_worker = SSHWorker()
        ssh_worker.ssh_signals.result.connect(MainWindow.ssh_result)
        self.ssh_threadpool.start(ssh_worker)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.button_compare = QPushButton('Compare')
        self.button_compare.clicked.connect(self.compare)
        self.setCentralWidget(self.button_compare)

    def compare(self):
        compare_thread = QThread(self)
        self.compare_worker = CompareWorker()

        compare_thread.started.connect(self.compare_worker.execute)
        self.compare_worker.done.connect(compare_thread.quit)
        self.compare_worker.done.connect(self.compare_worker.deleteLater)

        self.compare_worker.moveToThread(compare_thread)
        compare_thread.start()

    def ssh_result(self, server, message):
        print('server: ', server, ', result: ', message)


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()