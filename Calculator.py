class CalculatorClass:  # Класс для калькулятора
    def plus(self):
        a = int(input())
        b = int(input())
        return f'{a} + {b} = {a + b}'

    def minus(self):
        a = int(input())
        b = int(input())
        return f'{a} - {b} = {a - b}'

    def ymnojenie(self):
        a = int(input())
        b = int(input())
        return f'{a} * {b} = {a * b}'

    def delenie(self):
        try:
            a = int(input())
            b = int(input())
            return f'{a} / {b} = {a / b}'
        except ZeroDivisionError:
            print('На ноль делить нельзя!')

    def delenie_pomodul(self):
        try:
            a = int(input())
            b = int(input())
            return f'{a} % {b} = {a % b}'
        except ZeroDivisionError:
            print('На ноль делить нельзя!')

    def vozvedei_vstepen(self):
        a = int(input())
        b = int(input())
        return f'{a} ** {b} = {a ** b}'

    def celochislennoe_delenie(self):
        try:
            a = int(input())
            b = int(input())
            return f'{a} // {b} = {a // b}'
        except ZeroDivisionError:
            print('На ноль делить нельзя!')


calculator = CalculatorClass()


class MathematicalClass:  # Класс для математических функций
    def tabl(self):
        for i in range(1, 10):
            print('-' * 34)
            for y in range(1, 10):
                print(i * y, end="\t")
            print()


mathematical = MathematicalClass()


def cal():  # Калькулятор
    flag = input('Выберите операцию: +, -,  *, /, %, **, //: ')
    if flag == '+':
        print(calculator.plus())
    elif flag == '-':
        print(calculator.minus())
    elif flag == '*':
        print(calculator.ymnojenie())
    elif flag == '/':
        print(calculator.delenie())
    elif flag == '%':
        print(calculator.delenie_pomodul())
    elif flag == '**':
        print(calculator.vozvedei_vstepen())
    elif flag == '//':
        print(calculator.celochislennoe_delenie())
    else:
        print('Неправильный выбор операции!')


def mathemat():  # Математические функции
    flag_2 = input('''Математические функции:
    1 - Таблица умножения
    2 - что то еще
    3 - что то еще''')
    if flag_2 == '1':
        print(mathematical.tabl())

    else:
        print('Неправильный выбор операции!')


def vibor():  # Тут выбор на разные функции(далее будут добавлены другие программы)
    vibor_prog = input('''Выберите функционал: 
    1 - Калькулятор
    2 - Математические функции
    3 - Скачать весь ЮТУБ
    4 - Скорость интернета '''
                       )
    if vibor_prog == '1':
        cal()
    elif vibor_prog == '2':
        mathemat()
    elif vibor_prog == '3':
        pass
    elif vibor_prog == '4':
        pass


vibor()
# cal()


while True:  # Возврат к выбору функционала
    flag_3 = input('Еще раз: да / нет: ')
    if flag_3 == 'да':
        cal()
    elif flag_3 == 'нет':
        vibor()
    else:
        break

