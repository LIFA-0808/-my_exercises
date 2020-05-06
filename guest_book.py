file_name = 'guest_book.txt'

while True:
    name = input('Enter name or "q" for quit: ')
    if name != "q":
        with open(file_name, 'a') as file_obj:
            file_obj.write(name + '\n')
    else:
        break
