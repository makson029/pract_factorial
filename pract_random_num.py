import random

def user_number():
    secret_number = random.randint(1, 100)
    attempts_left = 10

    print(f"Я загадал число от 1 до 100. Попробуй угадать его за {attempts_left} попыток!")

    while attempts_left > 0:
        # Подсказка при остатке менее 5 попыток
        if attempts_left < 5:
            lower_bound = max(1, secret_number - 5)
            upper_bound = min(100, secret_number + 5)
            print(f"Загаданное число находится в диапазоне от {lower_bound} до {upper_bound}.")

        try:
            guess = int(input(f"Осталось попыток: {attempts_left}. Введите ваше предположение: "))
        except ValueError:
            print("Пожалуйста, введите целое число!")
            continue

        if guess < 1 or guess > 100:
            print("Число должно быть от 1 до 100!")
            continue

        if guess == secret_number:
            print("Поздравляю! Вы угадали число!")
            break
        elif guess < secret_number:
            print("Слишком маленькое число!")
        else:
            print("Слишком большое число!")
        
        attempts_left -= 1

    if attempts_left == 0:
        print(f"Вы не угадали число. Это было {secret_number}.")

user_number()

while True:
    play_again = input("Хотите сыграть ещё раз? (yes/no): ").strip().lower()
    if play_again in ("yes", "y"):
        user_number()
    elif play_again in ("no", "n"):
        print("Спасибо за игру!")
        exit()
    else:
        print("Пожалуйста, введите 'yes' или 'no'.")
