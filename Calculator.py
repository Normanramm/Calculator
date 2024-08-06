class ExampleClass:
    def plus(self):
        a = int(input())
        b = int(input())
        return a + b

    def minus(self):
        a = int(input())
        b = int(input())
        return a - b


example = ExampleClass()


def cal():
    flag = input('Выберите операцию: + или -: ')
    if flag == '+':
        print(example.plus())
    elif flag == '-':
        print(example.minus())
    else:
        print('Не то ввел!')


cal()
while True:
    flag_2 = input('Еще раз: да / нет: ')
    if flag_2 == 'да':
        cal()
    else:
        break