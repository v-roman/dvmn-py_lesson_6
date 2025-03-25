password = input('Введите пароль: ')

def is_very_long(password):
    if len(password) > 12:
        return True
    else:
        return False

def has_digit(password):
    for number in password:
        return any(number.isdigit() for number in password)

def has_letters(password):
    for letters in password:
        return any(letters.isalpha() for letters in password)

def has_upper_letters(password):
    for upper_letters in password:
        return any(upper_letters.isupper() for upper_letters in password)

def has_lower_letters(password):
    for lower_letters in password:
        return any(lower_letters.islower() for lower_letters in password)

def has_symbols(password):
    for symbols in password:
        return any(symbols.isalpha() == False and symbols.isdigit() == False for symbols in password)

function = [
    has_digit(password),
    is_very_long(password),
    has_letters(password),
    has_upper_letters(password),
    has_symbols(password),
]

score = 0
for i in function:
    if i == True:
        score = score + 2
    else:
        score = score

print('Рейтинг пароля:', score)
