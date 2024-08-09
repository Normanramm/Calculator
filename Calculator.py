class ExampleClass:
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

    def delenie_po_modul(self):
        try:
            a = int(input())
            b = int(input())
            return a % b
        except ZeroDivisionError:
            print('На ноль делить нельзя!')

    def vozvedei_v_stepen(self):
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


example = ExampleClass()


def cal():  # Калькулятор(тут дописать другие математические операции)
    flag = input('Выберите операцию: +, -,  *, /, %, **, //: ')
    if flag == '+':
        print(example.plus())
    elif flag == '-':
        print(example.minus())
    elif flag == '*':
        print(example.ymnojenie())
    elif flag == '/':
        print(example.delenie())
    elif flag == '%':
        print(example.delenie_po_modul())
    elif flag == '**':
        print(example.vozvedei_v_stepen())
    elif flag == '//':
        print(example.celochislennoe_delenie())
    else:
        print('Неправильный выбор операции!')


def vibor():  # Тут выбор на разные функции(далее будут добавлены другие программы)
    vibor = input('''Выберите функционал: 
    1 - Калькулятор
    2 - Таблица умножения
    3 - Математические функции'''
                  )
    if vibor == '1':
        cal()
    elif vibor == '2':
        print('тут будет таблица умножения')
    elif vibor == '3':
        print('тут будут математические функции и возможно сделать для них отдельный class')


vibor()
#cal()


while True:  # Возврат к выбору функционала
    flag_2 = input('Еще раз: да / нет: ')
    if flag_2 == 'да':
        cal()
    elif flag_2 == 'нет':
        vibor()
    else:
        break
