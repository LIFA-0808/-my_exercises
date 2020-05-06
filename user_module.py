"""module for importing"""


class User:
    """Creating profile"""
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
