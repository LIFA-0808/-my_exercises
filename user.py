class User:

    def __init__(self, first_name, last_name, age, hometown, field):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hometown = hometown
        self.field = field
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print('User name: ' + self.first_name.title() + ' ' + self.last_name.title(),
              'Age: ' + str(self.age),
              'Hometown: ' + self.hometown.title(),
              'Field: ' + self.field.lower(),
              sep='\n')

    def greet_user(self):
        print('Hello, ' + self.first_name.title() + ' ' + self.last_name.title())


class Privileges:
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


first_user = User('Ivan', 'Smirnov', '25', 'Moscow', 'manager')
first_user.describe_user()
first_user.greet_user()
second_user = User('kile', 'broflovski', 13, 'south park', 'pupil')
third_user = User('keny', 'mackormic', 100, 'new york', 'hero')
fourth_user = User('stan', 'newman', 14, 'NearWil', 'farmer')
fifth_user = User('eric', 'catrman', 13, 'buddhabox', 'fatguy')
second_user.greet_user()
second_user.describe_user()
third_user.greet_user()
third_user.describe_user()
fourth_user.greet_user()
fourth_user.describe_user()
fifth_user.greet_user()
fifth_user.describe_user()

# 9-4
print(str(first_user.login_attempts))
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
print(str(first_user.login_attempts))
first_user.reset_login_attempts()
print(str(first_user.login_attempts))
