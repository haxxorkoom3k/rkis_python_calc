def calc(a, b):
        return a / b

def call_calc():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        result = calc(a, b)
    except ValueError:
        raise ValueError('одно из введённых чисел не число')
    return result

print(call_calc())
