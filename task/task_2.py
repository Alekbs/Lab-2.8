#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def cylinder():
    i = input("Введите 1, если хоте получить только площадь боковой поверхности цилиндра\n"
              "Введите 2, если хотите получить полную площадь цилиндра\n")

    boc = 2*math.pi*r*h

    if i == '1':
        print("Площадь боковой поверхности цилиндра: ", boc)

    elif i == '2':
        print("Полная площадь цилиндра: ", boc + 2*circle())

    else:
        print("Введено неверное значение")

def circle():
    return (math.pi*pow(r, 2))

if __name__ == '__main__':
    r = float(input("Введите радиус круга: "))
    h = float(input("Введите высоту цилиндра: "))
    cylinder()
