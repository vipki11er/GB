# -*- coding: utf-8 -*-
"""
Created on 2022-Apr-25 
@author: Taranets
"""
import datetime
from datetime import datetime
from datetime import timedelta

starttime = datetime.now()
print("Поехали " + str(starttime))

t=int(input("Введите любое количество секунд для конвернтации в #дней и чч:мм:сс :"))
d=((t//86400))%30
h=((t//3600))%24
m=(t//60)%60
s=t%60
if h<10:
    h=str('0'+str(h))
else:
    h=str(h)
if m<10:
    m=str('0'+str(m))
else:
    m=str(m)
if s<10:
    s=str('0'+str(s))
else:
    s=str(s)
print("Сконвертировали :",str(d)+' day, '+str(h)+':'+str(m)+':'+str(s))

sec=int(input("Еще 1 попытка, вводим секундвы: "))
time_format = str(timedelta(seconds = sec))
print("Вот такой результат :-",time_format)


print("Закончили " + str(starttime))
