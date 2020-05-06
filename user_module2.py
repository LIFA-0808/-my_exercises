from user_module import User


class Privileges:
    """Adding privileges for admin"""
    def __init__(self, privileges=('разрешено добавлять сообщения',
                                   'разрешено удалять пользавателей',
                                   'разрешено банить пользователей')):
        self.privileges = privileges

    def show_privileges(self):
        print('Вам доступны действия: ' + ', '.join(self.privileges))


class Admin(User):
    """Describing Admin"""
    def __init__(self, first_name, last_name, age, hometown, field):
        super().__init__(first_name, last_name, age, hometown, field)
        self.privileges = Privileges()
