#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiply(count=1):
    num = float(input("Введите число: "))

    if num != 0:
        count *= num
        print ("Произведение: ", count)
        return multiply(count)

if __name__ == '__main__':
    multiply()
