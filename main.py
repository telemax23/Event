from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTreeWidgetItem
import time
import pymysql
import re
from db_config import *
import generate_password
from Class_Mysql import *
from Class_User import *
from Class_Processing import *
from Ui_Login import *
from Ui_Event_shedule import *
from Ui_Event import *
from Ui_Add_participant import *
from Ui_Analisis_list import *
from Ui_Accept_docs import *
from Ui_Create_event import *
from Ui_Create_participant import *
from Ui_Create_organization import *
from Ui_Create_inspector import *
from Ui_Create_user import *
from Ui_List_organization import *
from Ui_List_participants import *


class Login(Ui_Login):
    """Класс работы с окном Вход в программу"""

    def __init__(self):
        dialog = QDialog()
        super().setupUi(dialog)
        self.clicked_connect(dialog)
        dialog.show()
        app.exit(app.exec())

    def close_app(self):
        """Выход из программы по Закрытию окна"""
        journal.close_login()
        sys.exit(4)

    def clicked_connect(self, dialog):
        """Обработка нажатий кнопки Логин в окне 'Вход в программу'"""
        self.pushButton_login.clicked.connect(self.check_access)
        self.lineEdit_password.returnPressed.connect(self.check_access)

    def check_access(self):
        """Обработка входящих логина и пароля"""
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
        # Не верный пароль
        elif flag_access == 2:
            self.label_bad_password.setText("не верный")
            print(user_login['second_name'], user_login['first_name'], flag_access)


class Event_shedule(Ui_Event_shedule):
    """Класс работы с окном Расписание Мероприятий"""

    def __init__(self):
        window = QMainWindow()
        super().setupUi(window)
        self.username_login_role = access.get_username_and_role(user_login)
        self.label_username_login_role.setText(f'{self.username_login_role}')
        self.adjust_tree(self.tree_event_shedule)
        self.move_to_centre(window)
        self.clicked_connect(window)
        window.showMaximized()
        window.show()
        sys.exit(app.exec())

    def move_to_centre(self, window):
        """Выравниваем окно по центру экрана"""
        desktop = QApplication.desktop()
        desktop.screenGeometry()
        x = (desktop.width() - window.width()) // 2
        y = (desktop.height() - window.height()) // 2
        window.move(x, y)

    def close_app(self):
        """Выход из программы по Закрытию окна"""
        # разобраться, пока не работает
        journal.close_login()
        sys.exit(4)

    def adjust_tree(self, tree):
        """Установка наименований для колонок Tree"""
        columns_names = ['Мероприятие', 'Дата', 'Страна', 'Город', 'Участников', 'Организация', 'Статус']
        # tree.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        for i in columns_names:
            tree.headerItem().setText(columns_names.index(i), i)

    def clicked_connect(self, window):
        """Обращения к классам окон по клику мыши"""
        self.pushButton_exit.clicked.connect(self.close_shedule)
        self.pushButton_exit.clicked.connect(window.close)
        self.pushButton_create_event.clicked.connect(Create_Event)
        self.pushButton_create_participant.clicked.connect(Create_participant)
        self.pushButton_create_organization.clicked.connect(Create_organization)
        self.pushButton_create_inspector.clicked.connect(Create_inspector)
        self.pushButton_list_organization.clicked.connect(List_organization)
        self.pushButton_list_of_all_participants.clicked.connect(List_participants)
        self.pushButton_open_event.clicked.connect(Event)
        self.pushButton_export_xls.clicked.connect(window.showMaximized)
        self.pushButton_print.clicked.connect(Create_user)
        # self.pushButton_find_event.clicked.connect(self.tree_event_shedule.clear)
        # self.comboBox_event_status.currentIndexChanged['QString'].connect(self.tree_event_shedule.expandAll)

    def close_shedule(self):
        """Запись лога выхода, по нажатию на кнопку Выход"""
        journal.finish_log(f'{self.username_login_role}')


class Event(Ui_Event):
    """Работа с окном Мероприятие"""

    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.clicked_connect()
        dialog.exec()

    def clicked_connect(self):
        """Обработка нажатий кнопок"""
        self.pushButton_add_participance.clicked.connect(Add_participant)
        self.pushButton_analisis_doc.clicked.connect(Analisis_list)


class Analisis_list(Ui_Analisis_docs):
    """Класс работы с окном Анализ загруженных документов"""

    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.clicked_connect()
        dialog.exec()

    def adjust_tree(self, tree):
        """Установка наименований для колонок Tree"""
        columns_names = ['Телефон', 'Фамилия', 'Имя', 'Отчество', 'Паспорт', 'Прописка', 'ИНН', 'СНИЛС', 'Диплом',
                         'Сертификат', 'Согласие', 'Анкета', 'Договор', 'Акт', 'Отчет']
        # tree.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        for name in columns_names:
            tree.headerItem().setText(columns_names.index(name), name)

    def clicked_connect(self):
        """Обработка нажатий кнопок"""
        pass
        # self.pushButton_add_participance.clicked.connect(List_participants)
        self.pushButton_open_analisis_doc.clicked.connect(Accept_docs)


class Accept_docs(Ui_Accept_docs):
    """Окно Принятия или отклонения документов"""

    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.label_username_login_role.setText(f'{username_login_role}')
        # self.clicked_connect()
        dialog.exec()


class Add_participant(Ui_Add_participant):
    """Окно добавления участника в Мероприятие"""

    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.label_username_login_role.setText(f'{username_login_role}')
        # self.clicked_connect()
        dialog.exec()


class Create_Event(Ui_Create_event):
    """Работа с окном Создание Мероприятия"""

    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.clicked_connect()
        dialog.exec()

    def clicked_connect(self):
        self.pushButton_select_organization.clicked.connect(List_organization)


class Create_user(Ui_Create_user):
    """Окно создания Пользователя"""

    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.clicked_connect(dialog)
        dialog.exec()

    def clicked_connect(self, dialog):
        self.pushButton_generate.clicked.connect(self.generate_password)
        self.pushButton_save.clicked.connect(self.read_field)
        self.pushButton_save.clicked.connect(dialog.close)
        self.pushButton_cancel.clicked.connect(dialog.close)
        # self.checkBox_disabled_participant.stateChanged['int'].connect(dialog.show)

    def generate_password(self):
        passw = generate_password.generate()
        self.lineEdit_password.setText(f'{passw}')

    def read_field(self):
        new_user = {}
        new_user['phone_number'] = self.lineEdit_phone_number.text()
        new_user['second_name'] = self.lineEdit_second_name.text()
        new_user['first_name'] = self.lineEdit_first_name.text()
        new_user['last_name'] = self.lineEdit_last_name.text()
        new_user[
            'full_name'] = f"{self.lineEdit_second_name.text()} {self.lineEdit_first_name.text()} {self.lineEdit_last_name.text()}"
        new_user['role_id'] = 2  # admin
        new_user['email'] = self.lineEdit_email.text()
        new_user['city'] = self.lineEdit_city.text()
        new_user['password'] = self.lineEdit_password.text()
        new_user['comment'] = self.lineEdit_comment.text()
        new_user['disabled'] = False
        self.write_user_to_db(new_user)

    def write_user_to_db(self, new_user):
        sql = Mysql(host="127.0.0.1", user="admin", port=3306, password="gnt6al47", db_name="logistics_db")
        sql.create_user(new_user)


class Create_participant(Ui_Create_participant):
    """Класс создания нового участника"""

    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        self.dialog = QDialog()
        super().setupUi(self.dialog)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.checkBox_disabled_participant.setText("")
        self.clicked_connect(self.dialog)
        self.db = Mysql(host, port, user, password, db_name)
        self.dialog.exec()

    def clicked_connect(self, dialog):
        """Обработка нажатий кнопок окна создание Участника"""
        self.pushButton_generate.clicked.connect(self.generate_password)
        self.pushButton_save.clicked.connect(self.add_new_participant)
        self.pushButton_cancel.clicked.connect(dialog.close)
        # self.checkBox_disabled_participant.stateChanged['int'].connect(dialog.show)

    def add_new_participant(self):
        """Добавляет нового пользователя в базу данных"""
        phone_number = self.lineEdit_phone_number.text()
        second_name = self.lineEdit_second_name.text()
        first_name = self.lineEdit_first_name.text()
        last_name = self.lineEdit_last_name.text()
        email = self.lineEdit_email.text()
        city = self.lineEdit_city.text()
        password = self.lineEdit_password.text()
        comment = self.lineEdit_comment.text()
        disabled = self.checkBox_disabled_participant.isChecked()
        # print("add")
        role = "participant"
        full_name = second_name + " " + first_name + " " + last_name
        # Форматирование номера телефона
        phone_number = self.formating_phone(phone_number)
        if len(phone_number) == 11:
            try:
                self.db.add_participant(phone_number, second_name, first_name, last_name, role, full_name, email, city,
                                        password, comment, disabled)
                self.dialog.close()

            except Exception as ex:
                print("Error add new participant")
        else:
            self.lineEdit_phone_number.setPlaceholderText("ВВЕДИТЕ НОМЕР ТЕЛЕФОНА")

    def generate_password(self):
        """Генерация пароля по нажатию на кнопку"""
        passw = generate_password.generate()
        self.lineEdit_password.setText(f'{passw}')

    def formating_phone(self, phone_number):
        """Форматирование строки телефона"""
        phone_number = phone_number.replace('+7', '8').strip()
        symbols = ["-", "(", ")", " "]
        for symbol in symbols:
            if symbol in phone_number:
                phone_number = phone_number.replace(symbol, '')
        return phone_number


class Edit_participant(Ui_Create_participant):
    """Окно редактирования Участника"""

    def __init__(self, id_from_db, current_values):
        username_login_role = access.get_username_and_role(user_login)
        self.dialog = QDialog()
        super().setupUi(self.dialog)
        self.label_create_participant.setText("Редактирование участника")
        self.label_username_login_role.setText(f'{username_login_role}')
        self.id_from_db = id_from_db
        self.current_values = current_values
        self.db = Mysql(host, port, user, password, db_name)
        self.set_view()

        self.clicked_connect(self.dialog)
        self.dialog.exec()

    def clicked_connect(self, dialog):
        """Обработка нажатий кнопок окна Редактирование участника"""
        self.pushButton_generate.clicked.connect(self.generate_password)
        self.pushButton_save.clicked.connect(self.update_user)
        self.pushButton_cancel.clicked.connect(dialog.close)
        # self.checkBox_disabled_participant.stateChanged['int'].connect(dialog.show)

    def update_user(self):
        """Обновляет данные пользователя в базе данных"""
        values = []
        values.append(self.lineEdit_phone_number.text())
        values.append(self.lineEdit_second_name.text())
        values.append(self.lineEdit_first_name.text())
        values.append(self.lineEdit_last_name.text())

        # Составление Full_name по полученным данным:
        values.append(values[1] + " " + values[2] + " " + values[3])

        values.append(self.lineEdit_city.text())
        values.append(self.lineEdit_email.text())
        values.append(self.lineEdit_password.text())
        values.append(self.lineEdit_comment.text())

        # print(values)
        self.db.update_participant_by_id(self.id_from_db, values)
        self.dialog.close()
        # print("updated")

    def set_view(self):
        """Устанавливает в поля для ввода данные выбранного пользователя"""
        self.lineEdit_phone_number.setText(self.current_values[0])
        self.lineEdit_second_name.setText(self.current_values[1])
        self.lineEdit_first_name.setText(self.current_values[2])
        self.lineEdit_last_name.setText(self.current_values[3])
        self.lineEdit_email.setText(self.current_values[4])
        self.lineEdit_city.setText(self.current_values[5])
        self.lineEdit_password.setText(self.current_values[6])
        self.lineEdit_comment.setText(self.current_values[7])

    def generate_password(self):
        """Генерация пароля в окне Редактирования Участника"""
        passw = generate_password.generate()
        self.lineEdit_password.setText(f'{passw}')


class Create_organization(Ui_Create_organization):
    """Окно создания новой организации"""

    def __init__(self):
        dialog = QDialog()
        super().setupUi(dialog)
        username_login_role = access.get_username_and_role(user_login)
        self.label_username_login_role.setText(f'{username_login_role}')
        dialog.exec()


class Create_inspector(Ui_Create_inspector):
    """Окно создания инспектора"""

    def __init__(self):
        dialog = QDialog()
        super().setupUi(dialog)
        username_login_role = access.get_username_and_role(user_login)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.clicked_connect()
        dialog.exec()

    def clicked_connect(self):
        """Обработка нажатий кнопок в окне Создание Инспектора"""
        self.pushButton_select_organization.clicked.connect(List_organization)
        self.pushButton_generate.clicked.connect(self.generate_password)

    def generate_password(self):
        """Обработка нажатий кнопок в окне Создание Инспектора"""
        passw = generate_password.generate()
        self.lineEdit_password.setText(f'{passw}')


class List_organization(Ui_List_organization):
    """Окно выводит список всех Организаций"""

    def __init__(self):
        dialog = QDialog()
        super().setupUi(dialog)
        username_login_role = access.get_username_and_role(user_login)
        self.label_username_login_role.setText(f'{username_login_role}')

        self.clicked_connect(dialog)
        dialog.exec()

    def clicked_connect(self, dialog):
        """Обработка нажатий кнопок в окне List_organization"""
        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)
        self.pushButton_add_organization.clicked.connect(Create_organization)

    def set_headers(self, headers_names, tree):
        """Установка заголовков таблицы Списка Организаций"""
        tree.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        for header in headers_names:
            tree.headerItem().setText(headers_names.index(header), header)


class List_participants(Ui_List_participants):
    """Окно выводит список всех участников в БД, вне зависимости от мероприятий"""

    def __init__(self):
        dialog = QDialog()
        super().setupUi(dialog)
        self.set_username_login_role()
        # Установка соеденения с БД
        self.db = Mysql(host, port, user, password, db_name)
        # Установка заголовков для колонок  treeWidget
        headers_names = ['Телефон', 'Фамилия', 'Имя', 'Отчетство', 'Город', 'e-mail', 'Пароль', 'Комментарий']
        self.set_headers(headers_names, self.tree_participants_list)
        # Инициализация функции вывода списка всех участников
        self.set_view_of_all_participants()
        self.clicked_connect()
        dialog.exec()

    def set_username_login_role(self):
        """Показывает Имя и Роль пользователя запустившего программу"""
        username_login_role = access.get_username_and_role(user_login)
        self.label_username_login_role.setText(f'{username_login_role}')

    def clicked_connect(self):
        """Обработка нажатий кнопок в окне Список всех участников"""
        self.pushButton_create_participant.clicked.connect(Create_participant)
        self.pushButton_create_participant.clicked.connect(self.update_tree)
        self.pushButton_edit_participant.clicked.connect(self.edit_participant)
        self.pushButton_edit_participant.clicked.connect(self.update_tree)
        self.pushButton_delete_participant.clicked.connect(self.delete_participant)

    def edit_participant(self):
        """Открытие окна редактирования пользователя + получение данных по выбранному в QTreeWidget пользователю в виде списка"""
        try:
            item = self.tree_participants_list.currentItem()
            result_data = []
            for i in range(0, 8):
                item_string = item.text(i)
                result_data.append(item_string)
            id_from_db = self.db.get_participant_id(result_data[0])
            # print(id_from_db, result_data)
            Edit_participant(id_from_db, result_data)
        except Exception as ex:
            print("Error")

    def delete_participant(self):
        """Удаление выделенного участника"""
        item = self.tree_participants_list.currentItem()
        phone_number = item.text(0)
        id = self.db.get_participant_id(phone_number)

        self.db.delete_participant_by_id(id)
        self.update_tree()

    def update_tree(self):
        """Обновление общего списка участников (Аналогично функции set_view_of_all_participants, но с небольшими отличиями)"""
        self.tree_participants_list.clear()
        try:
            db = Mysql(host, port, user, password, db_name)
        except Exception as ex:
            print("Error update list participants")

        keys = ['phone_number', 'second_name', 'first_name', 'last_name', 'email', 'city', 'password', 'comment']
        table_name = "participants"
        all_participants = db.select_all_data(table_name)

        value = []
        for id in range(0, len(all_participants)):
            for key in keys:
                value.append(all_participants[id][key])
            item = QTreeWidgetItem(value)
            self.tree_participants_list.addTopLevelItem(item)
            value.clear()

    def set_headers(self, headers_names, tree):
        """Устанавливает заголовки колонок для Списка всех участников"""
        tree.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        for header in headers_names:
            tree.headerItem().setText(headers_names.index(header), header)

    def set_view_of_all_participants(self):
        """Отображение данных по всем участникам"""
        print("set_view отработала")
        keys = ['phone_number', 'second_name', 'first_name', 'last_name', 'email', 'city', 'password', 'comment']
        table_name = "participants"
        all_participants = self.db.select_all_data(table_name)

        value = []
        for id in range(0, len(all_participants)):
            for key in keys:
                value.append(all_participants[id][key])
            item = QTreeWidgetItem(value)
            self.tree_participants_list.addTopLevelItem(item)
            value.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_login = {}
    journal = Journal()
    processing = Processing()
    access = Access()
    user = User()
    Login()
    Event_shedule()
    sys.exit(app.exec())