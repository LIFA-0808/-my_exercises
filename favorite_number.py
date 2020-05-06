import json

file_name = 'favorite.json'


def get_fav_num():
    """Получает любимое число, если оно есть"""
    try:
        with open(file_name) as f_obj:
            fav_num = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return fav_num


def add_new_fav_num():
    """Добавляет любимое число"""
    new_fav_number = input('Enter favorite number: ')
    with open(file_name, 'w') as f_obj:
        json.dump(new_fav_number, f_obj)
    return new_fav_number


def show_fav_num():
    """Выводит любимое число пользователя"""
    fav_num = get_fav_num()
    if fav_num:
        print('I know your favorite number! It\'s ' + fav_num)
    else:
        fav_num = add_new_fav_num()
        print('Thank U. Now I know UR favorite number! It\'s ' + fav_num)


show_fav_num()
