from Class_Mysql import *
from Class_Access import *


class Processing:
    """Класс обработки данных"""
    def __init__(self):
        journal.log(f'----------Program started----------')

    def check_database_connection(self):
        """Если подключение к БД успешно, то запускаем программу, если нет, то сообщаем об отсутствии"""
        host = '127.0.0.1'
        port = 3306
        user = 'root'
        password = ''
        db_name = 'logistic'

        db = Mysql(host=host, port=port, user=user, password=password, db_name=db_name)
        db.add_user()
        # return database

        journal.log(f'Подключение к базе данных. Успешно проведено')

        #journal.log(f'База данных не обнаружена. Создайте базу данных. Завершение работы программы')

    def check_exist_user(self):
        """Если в БД существует хотя бы один пользователь, то запускаем. Если такого нет, то предлагаем создать"""
        pass

    def rename_file_client(self, documents_members):
        """Переименование документов загруженных участниками мероприятия"""
        pass

journal = Journal()