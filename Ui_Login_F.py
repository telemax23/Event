import sys

from PyQt5.QtWidgets import QApplication, QDialog
from Ui_Login import *
from Class_Access import *
import time


class Login(Ui_Login):
    def __init__(self):
        dialog = QDialog()
        super().setupUi(dialog)
        self.connect(dialog)
        dialog.show()
        app.exit(app.exec())

    def connect(self, dialog):
        self.pushButton_login.clicked.connect(self.check_access)
        self.lineEdit_password.returnPressed.connect(self.check_access)
        # self.pushButton_login.clicked.connect(dialog.close)

    def check_access(self):
        global user_login
        access = Access()
        phone_number = f'{self.lineEdit_login.text()}'
        password = f'{self.lineEdit_password.text()}'
        self.label_bad_password.setText('')
        self.label_user_not_found.setText('')
        user_login, flag_access = access.login(phone_number, password)

        # Вход, если логин и пароль верные
        if flag_access == 0:
            app.exit()
            return user_login

        # Номер телефона не найден в БД.
        elif flag_access == 1:
            self.label_user_not_found.setText("не найден")
            print(f'Выход из функции check_access (номер телефона не найден)')
            # sys.exit(1)

        # Не верный пароль
        elif flag_access == 2:
            self.label_bad_password.setText("не верный")
            # sys.exit(2)
            print(user_login['second_name'], user_login['first_name'], flag_access)




app = QApplication(sys.argv)
user_login = {}
login = Login()
print(f'{user_login} user_login из тела программы')
print(f'Выход из тела программы')
sys.exit(0)
