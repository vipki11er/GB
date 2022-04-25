# -*- coding: utf-8 -*-
"""
Created on 2022-Apr-25 
@author: Taranets
"""

from datetime import datetime
from datetime import date

starttime = datetime.now()
print("Поехали " + str(starttime))

a = 5
b = 10
print("A =", a, ",", "B =", b)
print("A + B =", a + b)
c = int(input("введите значение C: "))
print("A + B - C =", a + b - c)
name = str(input("Введите своё имя: "))
bd = int(input("Введите год своего рождения: "))
today = date.today()
age = today.year - bd
print(str(name)+", вам вероятно "+str(age)+" лет.")
print("Закончили " + str(starttime))
