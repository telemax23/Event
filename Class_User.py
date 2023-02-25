"""//////////////////////////////////////////////"""
""""////////------IMPORT CLASSES-------////////"""
"""//////////////////////////////////////////////"""

from Class_Access import *

class User:
    """Класс создания, редактирования, удаления, сохранения пользователя в БД"""
    def create(self, person, user_login):
        """Действие по клику на кнопку: Добавить нового пользователя"""

        "Check if?"
        username_login = user.name(user_login)
        new_user = {}
        new_user['id'] = person[0]
        new_user['lname'] = person[1]
        new_user['fname'] = person[2]
        new_user['mname'] = person[3]
        new_user['city'] = person[4]
        new_user['phone'] = person[5]
        new_user['email'] = person[6]
        new_user['password'] = person[7]
        new_user['role'] = person[8]
        new_user['full_name'] = f'{person[1]}_{person[2]}_{person[3]}'

        # Проверка прав на создание и запись пользователя в БД. Если роль Сисадмин или Админ, идет запись в БД
        flag_access = access.check_role_admin(user_login)

        if flag_access ==  True:
            self.phone = new_user.get('phone')
            self.full_name = new_user.get('full_name')

            #write_new_user_to_db()

            journal.log(f"{username_login} - создал(а) нового пользователя {self.phone} {self.full_name}")
            self.create_user_profile_folder()
        else:
            journal.log(f"{username_login} - не хвататет прав для создания нового пользователя {new_user.get('phone')} {new_user.get('full_name')}")

    def name(self, user_login):
        """Возвращает Фамилию и Имя пользователя из user_login"""
        username = f'{user_login[1]} {user_login[2]}'
        return username

    def create_user_profile_folder(self):
        """Создание профильной папки участника"""

        "Check if?"
        self.user_profile_folder = f'/home/logistics/{self.full_name}_{self.phone}'
        os.makedirs(self.user_profile_folder)
        journal.log(f'Создана профильная директория: {self.full_name}_{self.phone}')


user = User()
access = Access()