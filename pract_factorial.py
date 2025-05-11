import math

def calculate_factorial(n):
    # Возвращает факториал числа n.
    return math.factorial(n)

def get_positive_integer():
    # Запрашивает у пользователя положительное целое число.
    while True:
        user_input = input("Введите положительное целое число (или 'exit' для завершения): ").strip()
        
        if user_input.lower() == "exit":
            print("Программа завершена.")
            return None
        
        try:
            number = int(user_input)
            if number < 0:
                print("Ошибка: Вы ввели отрицательное число. Пожалуйста, введите положительное целое число.")
                continue
            return number
        except ValueError:
            print("Ошибка: Вы ввели не целое значение. Пожалуйста, введите положительное целое число.")

def main():
    while True:
        number = get_positive_integer()
        if number is None:
            break  # Завершить программу, если пользователь ввел "выход"
        
        result = calculate_factorial(number)
        print(f"Факториал числа {number} равен {result}.")

        continue_input = input("Хотите ввести еще одно число? (yes/no): ").strip().lower()
        if continue_input not in ("yes", "y"):
            print("Программа завершена.")
            break
        
main()