def is_very_long(password):
    return len(password) > 12

def has_digit(password):
    return any(number.isdigit() for number in password)

def has_letters(password):
    return any(letters.isalpha() for letters in password)

def has_upper_letters(password):
    return any(upper_letters.isupper() for upper_letters in password)

def has_lower_letters(password):
    return any(lower_letters.islower() for lower_letters in password)

def has_symbols(password):
    return any(symbols.isalpha() == False and symbols.isdigit() == False for symbols in password)

def main():
    password = input('Введите пароль: ')

    function = [
        has_digit(password),
        is_very_long(password),
        has_letters(password),
        has_upper_letters(password),
        has_symbols(password),
    ]

    score = 0
    for character in function:
        if character == True:
            score = score + 2
        else:
            score = score
    print('Рейтинг пароля:', score)

if __name__ == "__main__":
    main()
