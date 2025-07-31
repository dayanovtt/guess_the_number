import random

number = random.randint(0, 50)
counter = 0

while True:
    guess = int(input('Угадай число от 0 до 50: '))
    counter += 1
    if guess < number:
        print('Маловато')
    elif guess > number:
        print('Многовато')
    else:
        print(f'Поздравляю! Вы угадали число за {counter} попыток.')
        break