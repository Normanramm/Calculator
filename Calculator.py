class CalculatorClass:
    def plus(self):
        a = int(input())
        b = int(input())
        return a + b

    def minus(self):
        a = int(input())
        b = int(input())
        return a - b

    def ymnojenie(self):
        a = int(input())
        b = int(input())
        return a * b

    def delenie(self):
        try:
            a = int(input())
            b = int(input())
            return a / b
        except ZeroDivisionError:
            print('На ноль делить нельзя!')

    def delenie_pomodul(self):
        try:
            a = int(input())
            b = int(input())
            return a % b
        except ZeroDivisionError:
            print('На ноль делить нельзя!')

    def vozvedei_vstepen(self):
        a = int(input())
        b = int(input())
        return a ** b

    def celochislennoe_delenie(self):
        try:
            a = int(input())
            b = int(input())
            return a // b
        except ZeroDivisionError:
            print('На ноль делить нельзя!')


calculator = CalculatorClass()


def cal():  # Калькулятор(тут дописать другие математические операции)
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


def vibor():  # Тут выбор на разные функции(далее будут добавлены другие программы)
    vibor_prog = input('''Выберите функционал: 
    1 - Калькулятор
    2 - Математические функции
    3 - Скачать весь ЮТУБ
    4 - Скорость интернета'''
                       )
    if vibor_prog == '1':
        cal()
    elif vibor_prog == '2':
        pass
    elif vibor_prog == '3':
        pass
    elif vibor_prog == '4':
        pass


vibor()
# cal()


while True:  # Возврат к выбору функционала
    flag_2 = input('Еще раз: да / нет: ')
    if flag_2 == 'да':
        cal()
    elif flag_2 == 'нет':
        vibor()
    else:
        break

