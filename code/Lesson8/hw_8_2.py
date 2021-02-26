class Error(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def div(arg1, arg2):
        try:
            if arg2 == 0:
                raise Error('Деление на "0" не возможно!')
            else:
                return print(f'Результат: {arg1 / arg2:.2f}')
        except TypeError:
            return print('Неправильный тип элемента!')
        except Error as err:
            print(err)


Error.div(5, 'adfv')

