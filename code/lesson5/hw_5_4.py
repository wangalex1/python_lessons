import codecs
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file_4_1.txt', 'r') as file_obj:
    content = file_obj.read().splitlines()
    for i in content:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])
    print(new_file)

with codecs.open('file_4_new.txt', 'w', 'utf-8') as file_obj_2:
    file_obj_2.writelines('\n'.join(new_file))

