# -*- coding: utf-8 -*-
"""
Created on 2022-Apr-25 
@author: Taranets
"""
import datetime
from datetime import datetime

starttime = datetime.now()
print("Поехали " + str(starttime))

a = int(input("Вводим циферки :"))
b = 0
while a > 0:
    c = a % 10
    print("Рассматриваем цифру "+str(c))
    if c > b:
        b = c
        print("Найдена самая большая - "+str(b))
    a //= 10
    print("Осталось рассмотреть: "+str(a))
print ("Самое большое число - "+str(b))

numbers = int(input("Попробуем ввести список:"))
numlist = [int(n) for n in str(numbers)]
print("Получили список - "+str(numlist))
max_number = max(numlist)
print("Наибольшее число из списка: ", max_number)


print("Закончили " + str(starttime))