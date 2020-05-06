while True:
    try:
        number_1 = int(input('Enter the first number: '))
        number_2 = int(input('Enter the second number: '))
        result = number_1 + number_2
        print(str(number_1) + '+' + str(number_2) + '=' + str(result))
    except ValueError:
        print('Wrong number\'s format, try again')
