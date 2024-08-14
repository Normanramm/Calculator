class CalculatorClass:
    '''Класс для калькулятора(calculate)'''

    def __init__(self):
        self.operations = {
            "+": self.plus,
            "-": self.minus,
            "*": self.multiply,
            "/": self.divide,
            "%": self.modulo,
            "**": self.power,
            "//": self.floor_divide
        }

    def plus(self):
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        return f"{a} + {b} = {a + b}"

    def minus(self):
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        return f"{a} - {b} = {a - b}"

    def multiply(self):
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        return f"{a} * {b} = {a * b}"

    def divide(self):
        try:
            a = int(input("Введите делимое: "))
            b = int(input("Введите делитель: "))
            return f"{a} / {b} = {a / b}"
        except ZeroDivisionError:
            print("На ноль делить нельзя!")

    def modulo(self):
        try:
            a = int(input("Введите делимое: "))
            b = int(input("Введите делитель: "))
            return f"{a} % {b} = {a % b}"
        except ZeroDivisionError:
            print("На ноль делить нельзя!")

    def power(self):
        a = int(input("Введите основание: "))
        b = int(input("Введите степень: "))
        return f"{a} ** {b} = {a ** b}"

    def floor_divide(self):
        try:
            a = int(input("Введите делимое: "))
            b = int(input("Введите делитель: "))
            return f"{a} // {b} = {a // b}"
        except ZeroDivisionError:
            print("На ноль делить нельзя!")


class MathematicalClass:
    '''Класс для математических функций(math)'''

    def table(self):
        for i in range(1, 10):
            print('-' * 34)
            for y in range(1, 10):
                print(i * y, end="\t")
            print()


def calculate():  # Калькулятор
    operation = input("Выберите операцию: +, -, *, /, %, **, //: ")
    calculator = CalculatorClass()
    try:
        result = calculator.operations[operation]()
        print(result)
    except KeyError:
        print("Неправильный выбор операции!")


def math():  # Математические функции
    choice = input("""Математические функции:
    1 - Таблица умножения
    2 - Процентная ставка
    3 - что то еще""")
    mathematical = MathematicalClass()
    if choice == "1":
        print(mathematical.table())
    else:
        print("Неправильный выбор операции!")


def choose():  # Функция для выбора операции(наверно стоит засунуть в класс)
    choice = input("""Выберите функционал: 
    1 - Калькулятор
    2 - Математические функции
    3 - Скачать весь ЮТУБ
    4 - Голос робота
    4 - Скорость интернета """
                   )
    if choice == "1":
        calculate()
    elif choice == "2":
        math()
    elif choice == "3":
        pass
    elif choice == "4":
        pass

    while True:
        flag = input("Еще раз: да / нет: ")
        if flag == "да" and choice == '1':
            calculate()
        elif flag == 'да' and choice == '2':
            math()
        elif flag == "нет":
            choose()
        else:
            break


choose()
