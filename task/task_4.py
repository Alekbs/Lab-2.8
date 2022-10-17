#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    strok = input("enter a number: ")
    return strok


def test_input(strok):
    if type(strok) == int:
        return True
    elif strok.isnumeric():
        return True
    else:
        return False


def str_to_int(strok):
    a = int(strok)
    return a


def print_int(strok):
    print(strok)


if __name__ == '__main__':
    strok = get_input()
    pr = test_input(strok)
    if pr is True:
        print_int(str_to_int(strok))
    else:
        print("The entered string is not a number")