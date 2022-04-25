# -*- coding: utf-8 -*-
"""
Created on 2022-Apr-25 
@author: Taranets
"""
import datetime
from datetime import datetime

starttime = datetime.now()
print("Поехали " + str(starttime))

n=int(input("Поиграем? Введите любое число :"))
print("Вы ввели :"+str(n)+", и это Ваше 1-е число")
nn=str(n)+str(n)
print("Ваше 2-е число :"+str(nn))
nnn=str(n)+str(n)+str(n)
print("Ваше 3-е число :"+str(nnn))

s=int(n)
ss=int(nn)
sss=int(nnn)
summ=s+ss+sss

print("Результат игры: "+str(n)+"+"+str(nn)+"+"+str(nnn)+"="+str(summ))

print("Закончили играть " + str(starttime))