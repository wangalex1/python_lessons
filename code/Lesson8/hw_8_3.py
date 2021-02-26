class Checklist(Exception):
    def __init__(self, txt):
        self.txt = txt\


    @staticmethod
    def check_value():
        my_list = []
        while True:
            value = input('Введите элемент для добавление в список или "stop" для выхода: ')
            if value == 'stop':
                print(f'Текущий список: {my_list}')
                break
            try:
                if not value.isnumeric():
                    raise Checklist('Введено неправильное значение!')
                my_list.append(value)
            except Checklist as err:
                print(err)


Checklist.check_value()
