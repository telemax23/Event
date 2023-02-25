import pymysql
from db_config import host, port, password, db_name, user
class Mysql:
    """Подключение и работа с базой данных MqSql"""
    def __init__(self, host, port, user, password, db_name):
        try:
            self.connection = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor)
        except Exception as ex:
            print("Error connection to db")

    def select_all_data(self):
        """Получение всех строк из базы данных"""
        select_all_rows = f"SELECT * FROM 'users'"
        with self.connection.cursor() as cursor:
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            return rows

    def add_participant(self, phone_number, second_name, first_name, last_name, role, full_name, city, email, password, comment, disabled):
        """Добавление нового пользователя в базу данных MySql"""
        select_role_id = f"SELECT role_id FROM roles WHERE  role_name = '{role}'"
        with self.connection.cursor() as cursor:
            cursor.execute(select_role_id)
            result = cursor.fetchall()
            self.connection.commit()

        role_id = result[0]['role_id']

        insert_query = f"INSERT INTO participants (phone_number, second_name, first_name, last_name, full_name, role_id, city, email, password, comment,disabled) \
        VALUES('{phone_number}', '{second_name}', '{first_name}', '{last_name}', '{full_name}', {role_id}, '{city}', '{email}', '{password}', '{comment}',{disabled})"

        with self.connection.cursor() as cursor:
            cursor.execute(insert_query)
            self.connection.commit()

    def select_all(self, table_name):
        """Выбор всех строк из таблицы. Возвращает все строки"""
        select_all = f"SELECT * FROM {table_name}"
        with self.connection.cursor() as cursor:
            cursor.execute(select_all)
            result = cursor.fetchall()
            self.connection.commit()
        print(result)
        return result

    def get_participant_id(self, phone_number):
        """Получение ID участника по номеру телефона"""
        select_id = f"SELECT participant_id FROM participants WHERE phone_number = {phone_number}"
        with self.connection.cursor() as cursor:
            cursor.execute(select_id)
            result = cursor.fetchall()
            self.connection.commit()
        print(result)
        return result

    def delete_participant(self, id):
        """Удаление пользователя из БД MySql по id"""
        delete_quere = f"DELETE FROM participants WHERE participant_id = {id}"
        with self.connection.cursor() as cursor:
            print(cursor.execute(delete_quere))
            self.connection.commit()

    def __del__(self):
        """Закрытие сессии соединения с базой данных"""
        self.connection.close()


