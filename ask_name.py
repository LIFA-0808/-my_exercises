file_name = 'ur_name.txt'

name = input('Enter your name: ')
with open(file_name, 'w') as file_obj:
    file_obj.write(name)
