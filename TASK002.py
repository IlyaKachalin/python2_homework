"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""
n = int(input("Введите число (n). n =  "))

while 2**i <= n:
    print(i)
    i = i+1
