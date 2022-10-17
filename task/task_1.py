#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test():
    num = int(input("Введите целое число: "))

    if num >= 0:
        positive()

    if num < 0:
        negative()

def negative():
    print("Число отрицательное")

def positive():
    print("Число положительное")

if __name__ == '__main__':
    test()
