import json
profit = {}
prof = 0
i = 0
with open('file_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit[name] > 0:
            prof += profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
    pr = {'Средняя прибыль': round(prof_aver)}
    my_list = [profit, pr]
    print(f'Прибыль каждой компании:\n{my_list}')
with open('file_7.json', 'w') as write_js:
    json.dump(my_list, write_js)
    js_str = json.dumps(my_list)
    print(f'Создан файл с расширением json:\n{js_str}')
