with open('book.txt') as book:
    text = book.read().lower()
    print(text.count('the'))
