with open('file_1.txt', 'w') as my_f:
    line = input('Введите текст \n').split()
    for i in line:
        my_f.write(i + '\n')
        if not line:
            break

