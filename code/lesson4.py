#!/usr/bin/env python
# coding: utf-8

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# 
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
#     
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# In[1]:


def simple_calc():
    x = float(input('Введите количество отработанных часов : '))
    y = float(input('Введите суммы оплаты труда за 1 час : '))
    c = float(input('Укажите размер премии - '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы составил: {simple_calc() }')


# Другой вариант

# #### Можно просто просчитать с помощью калькулятора 

# In[28]:


from tkinter import *


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X^2"
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x550+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()


# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

# In[7]:


a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
answer = []

for i in range(len(a)-1):
    if a[i] < a[i+1]:
        answer.append(a[i+1])

print(answer)


# In[3]:


a = [1, 5, 1, 5, 1]
c= []
for i in range(len(a) - 1):
    n = a[i]
    i += 1
    m = a[i]
    if m > n:
        c.append(m)
print(c) 


# In[4]:


a = [1, 5, 1, 5, 1]
m = [j for i, j in zip(a, a[1:]) if j > i]


# In[5]:


print(m)


#   3.Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.

# In[10]:


for i in range(20,240):
    if i%20 ==0 or i%21 ==0 : #Если число кратно 20
        print(i) #то, вывести его


# In[29]:


for i in range(20,240):
    if i%20 ==0 or i%21 ==0 : #Если число кратно 20
        print(i) #то, вывести его


# In[30]:


data = [i for i in range(20, 240)if i%20 ==0 or i%21 ==0]  
print(data)


# In[31]:


my_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(f'Результат: {my_list}')


#  4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# 
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести
# 
# в порядке их следования в исходном списке. 
# 
# Для выполнения задания обязательно использовать генератор.

# In[12]:


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)


# 5. Реализовать формирование списка, используя функцию range() и
# 
# возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
# 
# Необходимо получить результат вычисления произведения всех элементов списка.
# 
# Подсказка: использовать функцию reduce().

# In[16]:


sum(i for i in range(100,1000) if i % 2 == 0)


# In[17]:


from functools import reduce


def my_func(arg1, arg2):
    return arg1 * arg2


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(f'Список: {my_list}')
print(f'Результат: {reduce(my_func, my_list)}')


# 6. Реализовать два небольших скрипта:
#     
# а) итератор, генерирующий целые числа, начиная с указанного,
# 
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# 
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, 
#     что создаваемый цикл не должен быть бесконечным.
#     Необходимо предусмотреть условие его завершения.

# In[21]:


from itertools import count, cycle
for el in count(3):
    if el == 10:
        break
    else:
        print(el)

print()

x = 0
for el2 in cycle('ABC'):
    if x == 10:
        break
    else:
        print(el2)
    x += 1


# 7. Реализовать генератор с помощью функции с ключевым словом yield, 
# 
# создающим очередное значение. При вызове функции должен создаваться объект-генератор. Функция должна вызываться
# 
# следующим образом: for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить 
#     
# только первые n чисел, начиная с 1! и до n!.
# 
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

# In[22]:


from itertools import count
from math import factorial


def fact():
    for el in count(1):
        yield factorial(el)


x = 0
for i in fact():
    if x == 10:
        break
    else:
        print(i)
    x += 1


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




