import sys
from PyQt5 import QtWidgets, uic

import socket

# class Connect:
#
#     sock = socket.socket()
#     sock.connect(('localhost', 8888))
#
#     def conv(data1):
#         return data1.encode('utf-8')
#
#     def deconv(data1):
#         return data1.decode('utf-8')
#
#     while True:
#         a = input()
#         sock.send(b'' + conv(a))
#         data = sock.recv(1024)
#         print(deconv(data))

class Window(QtWidgets.QMainWindow):

    def __init__(self):

        super(Window, self).__init__()

        self.ui = uic.loadUi('authorizationwindow.ui', self)
        self.ui.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.ok.clicked.connect(self.Login)
        self.ui.registration.clicked.connect(self.Registration)

    def Login(self):

        #запрос серверу о логине и пароле
        #если логин и пароль правильный, то статус успешно

        if (self.ui.login.text() == '111' and self.ui.password.text() == '222'):
              QtWidgets.QMessageBox.information(self, 'Статус','Успешно!')
              self.MainWindow()

        else:
             QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Неверный логин или пароль')

    def Registration(self):

        self.ui = uic.loadUi('registrationwindow.ui', self)
        self.ui.addpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        newlogin = self.addlogin.text()
        newpassword = self.addpassword.text()
        newemail = self.addemail.text()
        self.ui.newregistration.clicked.connect(self.addUser)
        self.ui.relogin.clicked.connect(self.ReLogin)


    def ReLogin(self):

        self.ui = uic.loadUi('authorizationwindow.ui', self)
        self.ui.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.ui.ok.clicked.connect(self.Login)
        self.ui.registration.clicked.connect(self.Registration)

    def addUser(self):

        # если соединение с сервером установлено, то
        # запрос передачи данных серверу newlogin = rLOGIN
        # запрос передачи данных серверу newpassword = rPASSWORD
        # запрос передачи данных серверу newemail = rEMAIL

        QtWidgets.QMessageBox.information(self,'Статус','Вы зарегистрировались!')

        #else:
        #      QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Соединение с сервером не установлено!')



    def MainWindow(self):


        self.ui = uic.loadUi('mainwindow.ui', self)

        # тут должен быть файл-таблица с аномальными данными!
        data = open('text.txt')
        self.adataview.addItems(data)


        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.GraphWidget, 0, 0)


        self.ui.setsensorperiod.clicked.connect(self.SetSensorPeriod)
        self.ui.diagnostic.clicked.connect(self.StartDiagnistic)

        # если соединение с сервером установлено, то
        # DATA получить данные с сервера о температуре установленного периода

        self.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])

        # else:
        #      QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Соединение с сервером не установлено!')

    def SetSensorPeriod(self):

        start = self.startperiod.text()
        end = self.endperiod.text()


        # если соединение с сервером установлено, то
        # запрос на установление периода отобажения данных
        # обновить данные в виджетах GraphWidget (график) и aDataView (таблица с аномальными данными)
        self.ui.setsensorperiod.clicked.connect()
        QtWidgets.QMessageBox.information(self, 'Статус','Новый период установлен!')
        # else:
        #      QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Соединение с сервером не установлено!')

    def Sampling(self):

        sampling = self.sampling.text()
        self.ui.setsampling.clicked.connect()


    def StartDiagnistic(self):

        # если соединение с сервером установлено, то
        # тут должен быть файл с информации о диагностике!
        self.adataview.clear()
        data = open('Diagnostic.txt',encoding='utf-8')
        self.adataview.addItems(data)

        QtWidgets.QMessageBox.information(self, 'Статус', 'Новый данные получены!')
        # else:
        #      QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Соединение с сервером не установлено!')

    def plot(self, hour, temperature):
        self.GraphWidget.plot(hour, temperature)

if __name__ == '__main__':

    import sys
    # connect = Connect()
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()



    sys.exit(app.exec_())