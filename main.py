from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTreeWidgetItem
import time
import pymysql
import generate_password
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


    def clicked_connect(self, dialog):
        """Обработка нажатий кнопки Логин в окне 'Вход в программу'"""
        self.pushButton_login.clicked.connect(self.check_access)
        self.lineEdit_password.returnPressed.connect(self.check_access)

    # def closeEvent(self, event):
    #     journal.close_login()
    #     # sys.exit(4)
    #     event.accept()

    def close_app(self):
        """Выход из программы по Закрытию окна"""
        journal.close_login()
        sys.exit(4)

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
            app.aboutToQuit.connect(self.close_app)


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
        columns_names = ['Телефон', 'Фамилия', 'Имя', 'Отчество', 'Паспорт', 'Прописка', 'ИНН', 'СНИЛС', 'Диплом', 'Сертификат', 'Согласие', 'Анкета', 'Договор', 'Акт', 'Отчет']
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
        self.pushButton_save.clicked.connect(dialog.show)
        self.pushButton_cancel.clicked.connect(dialog.close)
        # self.checkBox_disabled_participant.stateChanged['int'].connect(dialog.show)

    def generate_password(self):
        passw = generate_password.generate()
        self.lineEdit_password.setText(f'{passw}')


class Create_participant(Ui_Create_participant):
    """Класс создания нового участника"""
    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.label_username_login_role.setText(f'{username_login_role}')
        self.checkBox_disabled_participant.setText("")
        self.clicked_connect(dialog)
        dialog.exec()

    def clicked_connect(self, dialog):
        """Обработка нажатий кнопок окна создание Участника"""
        self.pushButton_generate.clicked.connect(self.generate_password)
        self.pushButton_save.clicked.connect(dialog.show)
        self.pushButton_cancel.clicked.connect(dialog.close)
        # self.checkBox_disabled_participant.stateChanged['int'].connect(dialog.show)

    def generate_password(self):
        """Генерация пароля по нажатию на кнопку"""
        passw = generate_password.generate()
        self.lineEdit_password.setText(f'{passw}')


class Edit_participant(Ui_Create_participant):
    """Окно редактирования Участника"""
    def __init__(self):
        username_login_role = access.get_username_and_role(user_login)
        dialog = QDialog()
        super().setupUi(dialog)
        self.label_create_participant.setText("Редактирование участника")
        self.label_username_login_role.setText(f'{username_login_role}')

        self.clicked_connect(dialog)
        dialog.exec()

    def clicked_connect(self, dialog):
        """Обработка нажатий кнопок окна Редактирование участника"""
        self.pushButton_generate.clicked.connect(self.generate_password)
        self.pushButton_save.clicked.connect(dialog.show)
        self.pushButton_cancel.clicked.connect(dialog.close)
        # self.checkBox_disabled_participant.stateChanged['int'].connect(dialog.show)

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

        # self.set_view_of_all_participants()

        self.clicked_connect()
        dialog.exec()

    def set_username_login_role(self):
        """Показывает Имя и Роль пользователя запустившего программу"""
        username_login_role = access.get_username_and_role(user_login)
        self.label_username_login_role.setText(f'{username_login_role}')

    def clicked_connect(self):
        """Обработка нажатий кнопок в окне Список всех участников"""
        self.pushButton_create_participant.clicked.connect(Create_participant)
        self.pushButton_edit_participant.clicked.connect(Edit_participant)

    def set_headers(self, headers_names, tree):
        """Устанавливает заголовки колонок для Списка всех участников"""
        tree.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        for header in headers_names:
            tree.headerItem().setText(headers_names.index(header), header)

    def set_view_of_all_participants(self):
        """Отображение данных по всем участникам"""
        keys = ['phone_number', 'second_name', 'first_name', 'last_name', 'email', 'city', 'password', 'comment']
        table_name = "participants"
        all_participants = self.db.select_all(table_name)

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
