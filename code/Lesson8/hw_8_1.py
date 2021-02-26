class Data:

    @classmethod
    def extraction(cls, data):
        try:
            my_data = [int(i) for i in data.split('-')]
            print(f'Текущая дата: {my_data}')
        except ValueError:
            print('Введено неправильное число.')

    @staticmethod
    def validation(day, month, year):
        if 0 < day <= 31:
            if 0 < month <= 12:
                if 0 <= year <= 2021:
                    return f'Всё верно'
                else:
                    print('Не верно введён год!')
            else:
                print('Не верно введён месяц!')
        else:
            print('Не верно введён день!')


Data.extraction('15-12-2000')
print(Data.validation(10, 4, 1520))
