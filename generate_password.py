import random
from string import printable

def generate():
    """Функция генерации пароля"""
    simbols = []
    exept = ['l', 'o', 'i', 'I', 'O']
    for i in printable:
        if i >= 'a' and i <= 'z':
            if i not in exept:
                simbols.append(i)
        elif i >= 'A' and i <= 'Z':
            if i not in exept:
                simbols.append(i)
        elif i >= '1' and i <= '9':
            simbols.append(i)

    lenght = 0
    passw = []
    while lenght < 8:
        simbol = random.choice(simbols)
        passw.append(simbol)
        lenght += 1

    password = ''.join(passw)
    return password