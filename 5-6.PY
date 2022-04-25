# -*- coding: utf-8 -*-
"""
Created on 2022-Apr-25 
@author: Taranets
"""
import datetime
from datetime import datetime

starttime = datetime.now()
print("Поехали " + str(starttime))

rev = int(input("Укажите сумму выручки :"))
cost = int(input("Укажите сумму издержек :"))
pers = int(input("Укажите количество сотрудников :"))
profit = rev - cost
print("Прибыль = "+str(profit))
profitability:float = float(profit)/float(rev)
prof_y = "{:.2%}".format(profitability)
pers_profit = profit//pers
if rev > cost:
    print("Выручка больше издержек и рентабельность равна "+str(prof_y)+". Прибыль на на одного сотрудника равна "+str(pers_profit)+".")

if rev < cost:
    print("Издержки больше выручки")
if rev == cost:
    print("Выручка и издержки равны")

print("Закончили расчеты " + str(starttime))