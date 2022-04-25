# -*- coding: utf-8 -*-
"""
Created on 2022-Apr-25 
@author: Taranets
"""

from datetime import datetime

starttime = datetime.now()
print("Поехали " + str(starttime))
print("Оказывается вы спортсмен")
a = int(input("Сколько вы пробежали км в первый день "))
b = int(input("Какого результата вы хотиде достигнуть "))
c = 1
while a <= b:
    a = a + a * 0.10 
    c += 1
    if a >= b:
        print("Вы достигнете нужного результата на", c, "день")

print("Закончили бегать " + str(starttime))