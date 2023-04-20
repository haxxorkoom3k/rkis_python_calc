def calc(choice, a, b):
    if choice == 1:
        return a + b
    elif choice == 2:
        return a - b
    elif choice == 3:
        return a * b
    else:
        raise ValueError('некорректный выбор операции')

def call_calc():
    choice_lst = ['1', '2', '3']
    input_choice = input("Введите операцию\n1. Сложение\n2. Вычитание\n3. Умножение\nВаш выбор: ")
    if input_choice in choice_lst:
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            result = calc(int(input_choice), a, b)
        except ValueError:
            raise ValueError('одно из введённых чисел не число')
        return result
    else:
        return f"{input_choice} не операция."

print(call_calc())