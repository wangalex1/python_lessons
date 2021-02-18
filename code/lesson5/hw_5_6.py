import codecs
import re
subj = {}
with codecs.open('file_6.txt', 'r', 'utf-8') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        my_list = lecture + practice + lab
        subj[subject] = sum(map(int, re.findall(r'\d+', my_list)))
    print(f'Общее количество часов по предмету - \n {subj}')
