with open('file_2.txt', 'r') as my_f:
    content = my_f.readlines()
    print(f'Количество строк: {len(content)}')
    for i in range(len(content)):
        print(f'Количество слов: {i + 1} строке - {len(content[i].split())}')
